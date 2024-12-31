from itertools import cycle
import asyncio
from pathlib import Path
from typing import Optional

from qg_toolkit.qtweepy import twitter
from qg_toolkit.tools.qproxy import Proxy

TWITTERS_TXT = Path("twitters.txt")
PROXIES_TXT = Path("proxies.txt")
RESULTS_TXT = Path("results.txt")

for filepath in (TWITTERS_TXT, PROXIES_TXT, RESULTS_TXT):
    filepath.touch(exist_ok=True)

FIELDS = ("auth_token", "username", "password")
TWITTER_ACCOUNTS = qg_toolkit.qtweepy.twitter.account.load_accounts_from_file(TWITTERS_TXT, fields=FIELDS)
PROXIES = Proxy.from_file(PROXIES_TXT)

if not PROXIES:
    PROXIES = [None]

semaphore = asyncio.Semaphore(10)  # 限制同时执行 10 个任务


async def handle_account(
    proxy: Optional[Proxy],
    twitter_account: twitter.Account,
):
    async with semaphore, twitter.Client(
        twitter_account, proxy=proxy
    ) as twitter_client:
        try:
            await twitter_client.establish_status()

            if twitter_account.status != "GOOD":
                print(f"{repr(twitter_account)} {twitter_account.status}")
                return

            await twitter_client.request_user()

            if await twitter_client.totp_is_enabled():
                print(f"{repr(twitter_account)} TOTP 已启用.")
                return

            await twitter_client.enable_totp()
            print(
                f"{repr(twitter_account)} 启用了 TOTP."
                f"\n\tTOTP Secret: {twitter_account.totp_secret}"
                f"\n\t备份码: {twitter_account.backup_code}"
            )
            with open(RESULTS_TXT, "a") as results_file:
                results_file.write(
                    f"{twitter_account.auth_token},"
                    f"@{twitter_account.username},"
                    f"{twitter_account.totp_secret},"
                    f"{twitter_account.backup_code}\n"
                )
            await asyncio.sleep(1)

        except Exception as exc:
            print(f"{repr(twitter_account)} 无法启用 TOTP: {exc}")


async def main():
    tasks = []
    for proxy, twitter_account in zip(cycle(PROXIES), TWITTER_ACCOUNTS):
        task = handle_account(proxy, twitter_account)
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

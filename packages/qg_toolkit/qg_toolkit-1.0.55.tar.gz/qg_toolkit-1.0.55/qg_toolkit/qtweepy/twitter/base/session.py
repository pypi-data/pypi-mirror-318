from typing import Union

from curl_cffi import requests

from qg_toolkit.tools.qproxy import Proxy


# from better_proxy import Proxy


class BaseAsyncSession(requests.AsyncSession):
    """
    Базовая асинхронная сессия:
        - Принимает прокси в формате URL и better-proxy.
        - По умолчанию устанавливает версию браузера chrome120.
        - По умолчанию устанавливает user-agent под версию браузера chrome120.
    """

    proxy: Union[Proxy,None]
    DEFAULT_HEADERS = {
        "accept": "*/*",
        "accept-language": "en-US,en",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "connection": "keep-alive",
    }
    DEFAULT_IMPERSONATE = requests.BrowserType.chrome120

    def __init__(
        self,
        proxy: Union[Proxy,str] = None,
        **session_kwargs,
    ):
        self._proxy = None
        headers = session_kwargs["headers"] = session_kwargs.get("headers") or {}
        headers.update(self.DEFAULT_HEADERS)
        session_kwargs["impersonate"] = (
            session_kwargs.get("impersonate") or self.DEFAULT_IMPERSONATE
        )
        super().__init__(**session_kwargs)
        self.proxy = proxy

    @property
    def user_agent(self) -> str:
        return self.headers["user-agent"]

    @property
    def proxy(self) -> Union[Proxy,None]:
        return self._proxy

    @proxy.setter
    def proxy(self, proxy: Union[Union[Proxy,None],str]):
        if not proxy:
            self.proxies = {}
            return

        self._proxy = Proxy.from_str(proxy) if proxy else None
        self.proxies = {"http": self._proxy.as_url, "https": self._proxy.as_url}

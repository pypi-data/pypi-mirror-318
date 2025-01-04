import requests

def get_cf_token_on_sonic():
    """在sonic上解CF_TOKEN"""
    body = {
        "site_key": "6LcSxLwoAAAAANXNkGTUHXqfaw2V4nIArm6u4xfk",
        "target_url": "https://zealy.io/login",
    }
    r = requests.post("http://127.0.0.1:6666/solve", json=body)
    token = r.json()["token"]
    print("Solved :: " + token)
# get_cf_token_v2()
get_cf_token_on_sonic()
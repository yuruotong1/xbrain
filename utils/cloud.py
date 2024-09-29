import requests
import json

base_url = "https://cloud.xbrain.site"

def register_user(username, password):
    url = f"{base_url}/auth/v1/signup"

    payload = json.dumps({
        "username": username,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-device-id': '00123'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


if __name__ == "__main__":
    res = register_user("test", "test")
    print(res.text)

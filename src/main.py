import requests

headers = {
    "accept": "application/json"
}

cookies = {
    "my_cookie": "pokemon"
}

url = "https://httpbin.org/get"

res = requests.get(url, cookies=cookies)

print(res.text)
print(res.cookies)
import requests

headers = {
    "accept": "application/json"
}

cookies = {
    "my_cookie": "pokemon"
}

login_data = {
    "form": "1",
    "email": "pokemon@gmail.com",
    "pw": "tyba"
}

url_get = "https://httpbin.org/get"
# url_post = "https://httpbin.org/post"
# url_post = "http://localhost:8000/post" # for local
url_post = "http://httpbin/post" # through container

# res = requests.get(url_get, cookies=cookies)
res = requests.post(url_post, login_data, cookies=cookies)

print(res.text)
print(res.cookies)
print(res.status_code)
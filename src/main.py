import requests, pickle
import os

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

url_get = "http://httpbin/cookies"
# url_post = "https://httpbin.org/post"
# url_post = "http://localhost:8000/post" # for local
url_post = "http://httpbin/post" # through container
def save_cookie(cookie, filename="cookie.txt"):
    print("Saving cookies")
    with open(filename, "wb") as f:
        # pickle.dump(res_cookie.cookies, f)
        pickle.dump(cookie, f)

def load_cookie(filename="cookie.txt"):
    with open('cookie.txt', 'rb') as f:
        print("Loading cookies")
        new_session.cookies.update(pickle.load(f))

session = requests.session()
# res = requests.get(url_get, cookies=cookies)
# res_cookie = session.get("https://www.google.com/")
res_cookie = session.get("http://httpbin/cookies/set/sessioncookie/bleach12345'")



if not os.path.exists('cookie.txt'):
        save_cookie(session.cookies, "cookie.txt")

new_session = requests.session()
load_cookie()

res = new_session.post(url_post, login_data)
print(res.text)
print(res.status_code)

print(f"ARE THE COOKIES SAME for post? : {res.cookies == res_cookie.cookies}")
print(new_session.cookies)
print(res.cookies)

res = new_session.get(url_get)
print(res.text)
print(res.status_code)

print(f"ARE THE COOKIES SAME for get? : {res.cookies == res_cookie.cookies}")
print(new_session.cookies) # this holds the session cookie
print(res.cookies) # this shows empty 

print(res.json()) # this will show the session cookies


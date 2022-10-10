import asyncio
import aiohttp

import pickle
import redis


r = redis.Redis(host='redis', port="6379", db=0) # for container 
# r = redis.Redis(host='localhost', port="6380", db=0) # for local dev

def load_cookie_txt(filename="cookie.txt"):
    with open('cookie.txt', 'rb') as f:
        print("Loading cookies from text")
        return pickle.load(f)

def del_cookie():
    print("Deleting cookie")
    r.delete("cookie")
del_cookie()
    

def save_cookie(cookie):
    print("Saving cookies redis")
    print("we're saving this cookie", cookie, "--------", bytes(cookie, 'utf-8'))
    # r.set("cookie", bytes(cookie, 'utf-8'))


def load_cookie():
    # print("Loading cookies from redis")
    if r.get('cookie'):
        print("-----------from redis get--------------------------------------------------")
        cookie = r.get('cookie').decode()
        print(cookie)
        return {"Set-Cookie": cookie}
    cookie = aiohttp.CookieJar()
    print("cookie in load", cookie._cookies)
    return cookie

async def main():
    urls = [
        'http://httpbin/cookies/set/sessioncookie/bleach12345',
    ]
    # print([f"{i} -----" for i in aiohttp.CookieJar()], "\n\n")
    # print([aiohttp.CookieJar()._cookies], "\n\n")
    # print(load_cookie_txt())
    print()
    # print(load_cookie())
    # return
    for url in urls:
        async with aiohttp.ClientSession(cookies=load_cookie()) as s:
            print("session cookie jar", s.cookie_jar._cookies)
            # return 
            async with s.get(url) as r:
                print('JSON', await r.json())
                # we know cookies are store in session
                # print([f"{i} -----" for i in s.cookie_jar])
                # print(s.cookie_jar._cookies, "these are the cookies")
                # cookies = s.cookie_jar.filter_cookies('http://httpbin.org')
                cookies = s.cookie_jar._cookies['httpbin']
                print(s.cookie_jar._cookies.values())
                # print("output cookies", cookies)
                # save_cookie(r.json())
                save_cookie(f"{cookies.values()}")
                # print("cookie key", cookies.items())
                # # print(f"cookies is: {cookies}")
                # for i in s.cookie_jar:
                #     print("-------------------")
                #     print(i.value)
                #     print("-------------------")
                #     print("-------------------")
                # for key, cookie in cookies.items():
                #     print('Key: "%s", Value: "%s"' % (cookie.key, cookie.value))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
import asyncio
import aiohttp

import pickle
import redis


r = redis.Redis(host='redis', port="6379", db=0) # for container 
# r = redis.Redis(host='localhost', port="6380", db=0) # for local dev

def load_cookie(session_obj, filename="cookie.txt"):
    with open('cookie.txt', 'rb') as f:
        print("Loading cookies")
        return pickle.load(f)

def save_cookie(cookie):
    print("Saving cookies")
    r.set("cookie", cookie)

def load_cookie():
    r.get('cookie')

async def main():
    urls = [
        'http://httpbin.org/cookies/set?test=ok',
    ]
    print([f"{i} -----" for i in aiohttp.CookieJar()], "\n\n")
    print([aiohttp.CookieJar()._cookies], "\n\n")
    for url in urls:
        async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar()) as s:
            async with s.get(url) as r:
                print('JSON', await r.json())
                # we know cookies are store in session
                print([f"{i} -----" for i in s.cookie_jar])
                print(s.cookie_jar._cookies, "these are the cookies")
                cookies = s.cookie_jar.filter_cookies('http://httpbin.org')
                save_cookie(f"{cookies}")
                print(f"cookies is: {cookies}")
                for key, cookie in cookies.items():
                    print('Key: "%s", Value: "%s"' % (cookie.key, cookie.value))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
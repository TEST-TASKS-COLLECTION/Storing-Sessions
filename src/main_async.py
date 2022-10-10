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


async def main():
    urls = [
        'http://httpbin.org/cookies/set?test=ok',
    ]
    print("cookie jar", aiohttp.CookieJar())
    for url in urls:
        async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar()) as s:
            async with s.get(url) as r:
                print('JSON', await r.json())
                print(f"THe cookie jar is {s.cookie_jar.filter_cookies('http://')}")
                cookies = s.cookie_jar.filter_cookies('http://httpbin.org')
                save_cookie(f"{cookies}")
                print(f"cookies is: {cookies}")
                for key, cookie in cookies.items():
                    print('Key: "%s", Value: "%s"' % (cookie.key, cookie.value))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
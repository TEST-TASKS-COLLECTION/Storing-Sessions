# from main_async import r
import aiohttp
import asyncio
import redis

# print("the cookie is", r.get('cookie').decode())

async def main():
    print("safe: ", aiohttp.CookieJar()._cookies)
    print("unsafe: ", aiohttp.CookieJar(unsafe=True)._cookies)
    print("quote: ", aiohttp.CookieJar(quote_cookie=False)._cookies)
    print("dummy: ", aiohttp.DummyCookieJar())
    async with aiohttp.ClientSession() as session:
        await session.get(
            'http://httpbin.org/cookies/set?my_cookie=my_value')
        filtered = session.cookie_jar.filter_cookies(
            'http://httpbin.org')
        print(filtered)
        assert filtered['my_cookie'].value == 'my_value'
        async with session.get('http://httpbin.org/cookies') as r:
            json_body = await r.json()
            print(json_body)
            assert json_body['cookies']['my_cookie'] == 'my_value'
            
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
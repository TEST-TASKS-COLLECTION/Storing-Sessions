import asyncio
import aiohttp

import json

from datetime import timedelta

import pickle
import redis

r = redis.Redis(host='redis', port="6379", db=0)


def save_cookie(cookie):
	print("Saving cookies redis")
	print(cookie)
	print("we're saving this cookie", cookie, "--------", bytes(str(cookie), 'utf-8'))
	r.set("cookie", bytes(str(cookie), 'utf-8'))

def del_cookie():
	print("Deleting cookie")
	r.delete("cookie")
# del_cookie()

def load_cookie():
	# print("Loading cookies from redis")
	cookie = aiohttp.CookieJar()
	if r.get('cookie'):
		print("-----------from redis get--------------------------------------------------")
		got_cookie = r.get('cookie').decode().replace("'", '"')
		# cookie.update_cookies()
		our_cookie = json.loads(got_cookie)['cookies']
		# print("the decoded cookie is", got_cookie, type(got_cookie))
		# print("the decoded cookie in json", )
		print("loaded cookie------------------------>", our_cookie)
		print("pri", cookie._cookies)
		print("cookie in load: ", cookie._cookies)
		cookie.update_cookies(our_cookie)
		print("cookie in load: ", cookie._cookies)
		return cookie
	# cookie.update_cookies({"sessioncookie": "pokemon123"})
	print("cookie in load: ", cookie._cookies)
	print("cookie in load: ", cookie._cookies)
	return cookie


def create_session(headers={}, timeout=8, **kwargs):
	timeout_seconds = timeout
	session_timeout = aiohttp.ClientTimeout(
		total=timeout*1.5, 
		sock_connect=timeout_seconds, 
		sock_read=timeout_seconds
	)
	headers = {
		#'User-Agent': UserAgent().random,
		'Referer': 'https://www.google.com/',
		# 'Set-Cookie': "lolhead=bleach",
		**headers,
	}
	
	print("-"*25)
	print(headers)
	print("-"*25)
	
	return aiohttp.ClientSession(
		connector=aiohttp.TCPConnector(ssl=False), 
		timeout=session_timeout, 
		headers=headers,
		# cookie_jar = load_cookie()		
  # **kwargs
	)


async def session_maker():
	urls = [
		'http://httpbin/cookies/set/sessioncookie/bleach12345',
	]
	cookie = load_cookie()
	print("*"*30)
	print("load cookie", str(cookie))
	print("*"*30)
	# cookie = {
	#     "Set-Cookie": load_cookie()
	# }
	# cookie = {"Set-Cookie": "sessioncookie=bleach12345"}
	# async with create_session(kwargs = cookie) as session:
	async with create_session(cookie_jar = load_cookie()) as session:
		# session = session.update_cookies(cookie)
	# async with create_session(headers = cookie) as session:
		print("*-*-*")
		print("COokie jar", session.cookie_jar)
		print("*-*-*")
		print("session cookie inside session: ", session.cookie_jar._cookies)
		async with session.get(urls[0]) as r:
			cookie = await r.json()
			# save_cookie(cookie)
			print(cookie)
			


loop = asyncio.get_event_loop()
loop.run_until_complete(session_maker())
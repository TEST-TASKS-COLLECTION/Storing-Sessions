from main_async import r
from main_async import load_cookie_txt
from main_async import load_cookie

print(r.get("cookie"))

print(load_cookie_txt())
print(load_cookie_txt()._cookies)
print(type(load_cookie_txt()))

print(load_cookie())
print(type(load_cookie()))
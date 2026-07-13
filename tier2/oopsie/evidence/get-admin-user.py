#!/usr/bin/env python3
import requests

url = "http://megacorp.com/cdn-cgi/login/admin.php"
cookies = {"role": "user", "value": "2233"}  # parse from cookie.txt if needed

#contents = ["uploads", "..", "../..", "/etc/passwd", "admin", "config"]

# for n in range(2233):
r = requests.get(url, params={"content": "uploads"}, cookies=cookies)
print(f"[bytes={len(r.content)}] [status={r.status_code}] content={"uploads"}")
#print(dir(r))
print(r.content)
    
    # Show a snippet of the response
    # print(r.text[:200])

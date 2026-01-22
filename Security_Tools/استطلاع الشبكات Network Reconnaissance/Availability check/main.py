# معرفة حالة الموقع هل هو يعمل او لا و معرفة سبب العطل (is it down)

import requests

url = "http://testphp.vulnweb.com"
response = requests.get(url, timeout=5)
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print("OK", url, "UP", response.status_code)
except requests.ConnectionError:
    print("NO", url, "Down", response.status_code)
except :
    print("Error")

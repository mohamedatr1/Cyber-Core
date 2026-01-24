# حظر الطلبات المشبوهة و منع استكشاف المسارات الحساسة

import requests 
import time

search = ["atr.html","login.php","main.txt","admin.php"]

url = "http://localhost/pycyber1/"

for x in search:
    full_url = url + x
    response = requests.get(full_url)
    if response.status_code == 200:
        print(f"[+]Found : {full_url} | code : {response.status_code}")
    else:
        print(f"[-]Not Found : {full_url} | code : {response.status_code}")
print(response.text)


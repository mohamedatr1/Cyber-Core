# https://jsonplaceholder.typicode.com/

#جلب البيانات من صفحات الويب باستخدام get()

import requests
url = "https://jsonplaceholder.typicode.com/comments/33"

response = requests.get(url)

if response.status_code == 200:
    print("information get")
    print(response.json())
else :
    print("Error!")
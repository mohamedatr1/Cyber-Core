# https://jsonplaceholder.typicode.com/
#التفاعل مع الواجهات البرمجية API عن طريق Post,Get
import requests
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title:" : "test",
    "user ID:" : 1,
    "body:" : "ATR",
}

response = requests.post(url,data)

print("code status: ",response.status_code)
print("response: ",response.json())
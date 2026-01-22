# تحميل الملفات من الانترنت (Get مع response.content)
import requests
file_url = "http://testphp.vulnweb.com/admin/create.sql"
response = requests.get(file_url)

if response.status_code == 200:
    with open("File interaction/download_dat.sql","wb") as file:
        file.write(response.content)
    print("OK")
else:
    print("Error")

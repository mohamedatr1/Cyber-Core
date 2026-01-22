import requests
#جمع المعلومات عن السيرفر باستخدام head() لجمع headers + items()
# http://testphp.vulnweb.com/

url = "http://testphp.vulnweb.com/"

response = requests.head(url)
print("information: ")

# {
#     key:value
# }

for key,value in response.headers.items():
    print(f"{key} : {value}")

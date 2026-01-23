import requests
from rich import print
def update_script():
    url = "http://localhost/cyber/script2.py"
    response = requests.get(url)
    if response.status_code == 200:
        with open(__file__,"wb") as file:
            file.write(response.content)
        print("[+] Have new update v2")
    else:
        print("[-] No update found")

update_script()

print("-------------------")
print("+     [yellow]Welcome[/]     +")
print("-------------------")
name = input("Enter your Name: ")
print(f"[blue]Your name is: [/] {name}")
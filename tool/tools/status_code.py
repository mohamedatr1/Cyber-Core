import requests

def status_code():
    url = input("Enter the Url link: ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] {url} is UP {response.status_code}")            
        else:
            pass
    except requests.exceptions.RequestException:
        print(f"[-] {url} is Down ")

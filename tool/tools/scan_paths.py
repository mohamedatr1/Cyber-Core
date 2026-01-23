import requests

def scan_paths():
    url = input("Enter the link: ")
    paths = ["text.txt","sls.php","awkds.html","test.php"]
    for  path in paths:
        full_url = f"{url}/{path}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"[+] Found : {url} | {path} | status code : {response.status_code}")
        else:
            print(f"[-] Not Found : {full_url}")
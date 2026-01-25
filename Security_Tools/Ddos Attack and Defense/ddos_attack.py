import requests
import threading
url = "http://localhost/pycyber1/site.php"
num_requests = 1000
num_threads = 100

def send_requests():
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            print(f"[+] - started : {url} | {response.status_code}")
        except requests.exceptions.RequestException:
            print("[-] Error Request") 

thread = [threading.Thread(target=send_requests) for _ in range(num_threads)]

for th in thread:
    th.start() 
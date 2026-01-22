# كشف التكنولوجيا المستخدمة في موقع معين 
import requests
from rich import print
url = "https://jsonplaceholder.typicode.com/"

response = requests.get(url)

if response.status_code == 200:
    print("[bold red on white]Technology Enumeration[/] :")
    for x,y in response.headers.items():
        # server : server type
        print(f"[bold yellow]{x}[/]: [bold green]{y}[/]")
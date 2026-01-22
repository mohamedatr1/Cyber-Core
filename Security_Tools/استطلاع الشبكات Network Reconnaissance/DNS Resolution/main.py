# معرفة IP السيرفر لموقع معين لفحص المنافذ المفتوحة

import requests
import socket
from rich import print
url = "http://testphp.vulnweb.com"
domian = "testphp.vulnweb.com"
ip = socket.gethostbyname(domian)
response = requests.get(url, timeout=5)
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print(f"[bold green]Ok[/] [italic blue] {url}[/] UP [bold red] {response.status_code}[/] [bold white on red] {ip}[/]")
except requests.ConnectionError:
    print("NO", url, "Down", response.status_code)
 
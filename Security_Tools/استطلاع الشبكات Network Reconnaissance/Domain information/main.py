# جلب معلومات WHOIS عن موقع معين
import requests
domian = "testphp.vulnweb.com/admin/"

response = requests.get(f"https://api.whois.vu./?q={domian}")

if response.status_code == 200:
    print(response.text)
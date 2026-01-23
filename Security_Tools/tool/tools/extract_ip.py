import socket

def extract_ip():
    print("-" * 20)
    print("+    IP Adress    +")
    print("-" * 20)
    hostname = input("Enter url Site: ")
    ip_adress = socket.gethostbyname(hostname)
    print(f"[+] IP is : {ip_adress}")
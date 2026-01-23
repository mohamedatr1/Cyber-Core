import requests
import sys
url = "http://localhost/cyber/password.txt"

def check_password(password):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            passwords = response.text.splitlines()
            if password in passwords:
                return True
            else:
                sys.exit(1)
        else:
            sys.exit(1)
    except:
        sys.exit(1)
if __name__ == "__main__":
    print("Welcome")
    password = input("Enter your password: ")
    check_password(password)
    print("-" * 20)
    print("Welcome to my program")

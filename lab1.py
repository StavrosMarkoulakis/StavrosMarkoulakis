import requests
from http import cookies
from datetime import datetime

def print_headers(response):
    print("Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

def print_server_software(response):
    print("\nServer Software:")
    server = response.headers.get("Server")
    if server:
        print(server)
    else:
        print("Server software information not available.")

def print_cookies(response):
    print("\nCookies:")
    cookie_header = response.headers.get("Set-Cookie")
    if cookie_header:
        cookie = cookies.SimpleCookie()
        cookie.load(cookie_header)
        for key, morsel in cookie.items():
            print(f"Name: {morsel.key}")
            expires = morsel["expires"]
            if expires:
                expires = datetime.strptime(expires, "%a, %d-%b-%Y %H:%M:%S %Z")
                duration = expires - datetime.now()
                print(f"Expires in: {duration}")
            else:
                print("Expires: Session cookie")
    else:
        print("No cookies found.")

def main():
    url = input("Enter the URL: ")
    response = requests.get(url)
    
    print_headers(response)
    print_server_software(response)
    print_cookies(response)

if __name__ == "__main__":
    main()

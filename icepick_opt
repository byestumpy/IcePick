import socket
import requests
from colors import *

def port_scanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
    except socket.error:
        print("Error occurred while scanning the port")
        
def scan(ip):
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        dns = data.get("hostname", "N/A")
        proxy = data.get("proxy", "N/A")
        vpn = data.get("security", {}).get("vpn", "N/A")
        location = f"{data.get('city', '')}, {data.get('region', '')}, {data.get('country_name', '')}"
        isp = data.get("org", "N/A")

        print(f"IP: {ip}")
        print(f"DNS: {dns}")
        print(f"Proxy: {proxy}")
        print(f"VPN: {vpn}")
        print(f"Location: {location}")
        print(f"ISP: {isp}")
    else:
        print(f"Error: {response.status_code}")



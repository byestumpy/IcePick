import sys
import time
import os
import requests
from def_core import *
from packaging import version
from pystyle import Anime, Write, Colorate, Colors, Box, Center

current_version = '1.0.0'  

def header():
    print(Center.XCenter(Colorate.Vertical(Colors.blue_to_white, """

 ██▓ ▄████▄  ▓█████  ██▓███   ██▓ ▄████▄   ██ ▄█▀
▓██▒▒██▀ ▀█  ▓█   ▀ ▓██░  ██▒▓██▒▒██▀ ▀█   ██▄█▒ 
▒██▒▒▓█    ▄ ▒███   ▓██░ ██▓▒▒██▒▒▓█    ▄ ▓███▄░ 
░██░▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▄█▓▒ ▒░██░▒▓▓▄ ▄██▒▓██ █▄ 
░██░▒ ▓███▀ ░░▒████▒▒██▒ ░  ░░██░▒ ▓███▀ ░▒██▒ █▄
░▓  ░ ░▒ ▒  ░░░ ▒░ ░▒▓▒░ ░  ░░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ▒ ░  ░  ▒    ░ ░  ░░▒ ░      ▒ ░  ░  ▒   ░ ░▒ ▒░
 ▒ ░░           ░   ░░        ▒ ░░        ░ ░░ ░ 
 ░  ░ ░         ░  ░          ░  ░ ░      ░  ░    
    ░                            ░                
                  Version 1.0.0                                                                                                                               
    """, 1)))
    
def socials():
    print(Center.XCenter(Colorate.Vertical(Colors.blue_to_white, """
Discord: Stumpy#1028
Telegram: byestumpy
themysteryinc.net

""", 5)))
    
header()
socials()

      
def perform_update():
    update_url = "https://github.com/byestumpy/IcePick/raw/main/icepick.py"

    response = requests.get(update_url)
    if response.status_code == 200:
        updated_script = response.text
        icepick_filename = "icepick.py"

        with open(icepick_filename, "w", encoding="utf-8") as file:
            file.write(updated_script)

        print("Update successful. Please restart the script.")
        sys.exit()
    else:
        print("Failed to download the updated script. Update aborted.") 
                   
def check_for_updates(current_version):
    url = "https://raw.githubusercontent.com/byestumpy/IcePick/main/version.txt"
    response = requests.get(url)
    latest_version = response.text.strip()

    if version.parse(current_version) < version.parse(latest_version):
        print(green + "An update is available!" + nc)
        print(green + f"Current version: {current_version}, Latest version: {latest_version}" + nc)
        
        while True:
            answer = input(cyan + "Would you like to update now? " + nc + yellow + "[" + nc + white + "y/n" + nc + yellow + "] " + nc).lower()
            
            if answer == "y":
                perform_update()
                print(icon + green + "Updating..." + nc)
                time.sleep(2.5)
                print(icon + green + "Update successful. Please restart the script." + nc)
                sys.exit()
            elif answer == "n":
                print(icon + green + "Skipping update." + nc)
                break
            else:
                print("Please enter a valid option.")
    else:
        print(icon + bcyan + "You have the most recent version!" + nc)

    
def start():
    steps = [
        ("Validating libraries...", 2.5),
        ("Checking for updates...", 3.0),
        ("Waking up the eskimos...", 0.5),
        ("Starting IcePick...", 0.5)
    ]
    
    for message, sleep_time in steps:
        print(icon + bcyan + message + nc)
        time.sleep(sleep_time)
    
    os.system('cls')
    header()
    socials()
    choose_option()

      
answer = input(cyan + "Start IcePick? " + nc + yellow + "[" + nc + white + "y/n" + nc + yellow + "] " + nc)
while answer.lower() not in ("y", "n"):
    print("Please enter a valid option.")
    answer = input(cyan + "Start IcePick? " + nc + yellow + "[" + nc + white + "y/n" + nc + yellow + "] " + nc)
if answer.lower() == "y":
    start()
elif answer.lower() == "n":
    sys.exit()
    

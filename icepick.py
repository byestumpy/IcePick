import sys
import time
import os
import requests
from packaging import version
from pystyle import Anime, Write, Colorate, Colors, Box, Center


black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

icon = yellow + "[" + nc + nc + "+" + nc + yellow + "] " + nc



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

def main():
      print("Hello")
      
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
        print(green + "Update to the latest version here: " + nc + bcyan + "https://github.com/byestumpy/IcePick/blob/main/update.txt" + nc)

        answer = input(cyan + "Would you like to update now? " + nc + yellow + "[" + nc + white + "y/n" + nc + yellow + "] " + nc)
        while answer.lower() not in ("y", "n"):
            print("Please enter a valid option.")
            answer = input(cyan + "Would you like to update now? " + nc + yellow + "[" + nc + white + "y/n" + nc + yellow + "] " + nc)
        if answer.lower() == "y":
            perform_update()
            print(icon + bcyan + "Updating..." + nc)
            time.sleep(2.5)
            print(icon + bcyan + "Update successful. Please restart the script." + nc)
            sys.exit()
        elif answer.lower() == "n":
            print(icon + bcyan + "Skipping update." + nc)
    else:
        print(icon + bcyan + "You have the most recent version!" + nc)
current_version = '1.5.0'      
def start():
      print(icon + bcyan + "Validating libraries..." + nc)
      time.sleep(2.5)
      print(icon + bcyan + "Checking for updates..." + nc)
      check_for_updates(current_version)
      time.sleep(3.0)
      print(icon + bcyan + "Waking up the eskimos..." + nc)
      time.sleep(0.5)
      print(icon + bcyan + "Starting IcePick..." + nc)
      time.sleep(0.5)
      # os.system('cls')
      main()
      





      
answer = input(cyan + "Start IcePick? " + nc + yellow + "[" + nc + white + "y/n" + nc + yellow + "] " + nc)
while answer.lower() not in ("y", "n"):
    print("Please enter a valid option.")
    answer = input(cyan + "Start IcePick? " + nc + yellow + "[" + nc + white + "y/n" + nc + yellow + "] " + nc)
if answer.lower() == "y":
    start()
elif answer.lower() == "n":
    sys.exit()
    

from colors import *
import os
import sys
import time
import requests
from icepick_opt import *
from def_core_icepick import IcePick
from packaging import version
from pystyle import Colorate, Colors, Box, Center

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
    
def option_1():
    shell = IcePick(header)
    shell.cmdloop()
    return
def option_2():
    target_host = input("Enter the target host: ")
    target_port = int(input("Enter the target port: "))
    port_scanner(target_host, target_port)
def option_3():
    print("Executing Option 1")
def option_4():
    print("Executing Option 2")
def option_5():
    print("Executing Option 1")
def option_6():
    print("Executing Option 2")
def option_7():
    print("Executing Option 1")
def option_8():
    print("Executing Option 2")
def option_9():
    print("Executing Option 1")
def option_10():
    print("Executing Option 2")
def option_11():
    print("Executing Option 1")
def option_12():
    print("Executing Option 2")
def option_00():
    print("Executing Option 1")
def option_99():
    print("Executing Option 2")
    
def choose_option():
    output = (
        f"{num_ico_l}01{num_ico_r}{bblue}IceShell\t{num_ico_l}04{num_ico_r}{bblue}Option 4\t{num_ico_l}07{num_ico_r}{bblue}Option 7\t{num_ico_l}10{num_ico_r}{bblue}Option 10\n"
        f"{num_ico_l}02{num_ico_r}{bblue}PortScan\t{num_ico_l}05{num_ico_r}{bblue}Option 5\t{num_ico_l}08{num_ico_r}{bblue}Option 8\t{num_ico_l}11{num_ico_r}{bblue}Option 11\n"
        f"{num_ico_l}03{num_ico_r}{bblue}Option 3\t{num_ico_l}06{num_ico_r}{bblue}Option 6\t{num_ico_l}09{num_ico_r}{bblue}Option 9\t{num_ico_l}12{num_ico_r}{bblue}Option 12\n"
        f"{num_ico_l}00{num_ico_r}{bblue}About\t{num_ico_l}99{num_ico_r}{bblue}Help\t{nc}"
    )

    options = [
        {"number": "01", "description": "IceShell", "function": option_1},
        {"number": "02", "description": "PortScan", "function": option_2},
        {"number": "03", "description": "Option 3", "function": option_3},
        {"number": "04", "description": "Option 4", "function": option_4},
        {"number": "05", "description": "Option 5", "function": option_5},
        {"number": "06", "description": "Option 6", "function": option_6},
        {"number": "07", "description": "Option 7", "function": option_7},
        {"number": "08", "description": "Option 8", "function": option_8},
        {"number": "09", "description": "Option 9", "function": option_9},
        {"number": "10", "description": "Option 10", "function": option_10},
        {"number": "11", "description": "Option 11", "function": option_11},
        {"number": "12", "description": "Option 12", "function": option_12},
        {"number": "99", "description": "Option 99", "function": option_99},
        {"number": "00", "description": "Option 00", "function": option_00},
    ]

    option_dict = {option["number"]: option for option in options}

    print(output)
    while True:
        choice = input(cyan + "Choose an option: " + nc + yellow + nc)
        if choice in option_dict:
            option_dict[choice]["function"]()
            return
        elif choice.lstrip("0") in option_dict:
            option_dict[choice.lstrip("0")]["function"]()
            return
        print(icon + bcyan + "Invalid option. Please try again." + nc)

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
        if message == "Checking for updates...":
            check_for_updates(current_version)
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

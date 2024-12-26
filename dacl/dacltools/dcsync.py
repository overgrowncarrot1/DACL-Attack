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
N = "-u '' -p ''"  # Null credentials
UP = f"-u {USER} -p {PASS}" if USER and PASS else None
UH = f"-u {USER} -H {HASH}" if USER and HASH else None
ENUMSMB = "--shares --users --interfaces --sessions --disks --loggedon-users --groups --computers --local-groups --pass-pol --rid-brute 5000"
ENUMLDAP = "--trusted-for-delegation --password-not-required --admin-count --users --groups --dc-list --get-sid --active-users"
ENUMNFS = "--shares"
ENUMFTP = "--ls"
ENUMVNC = "--screenshot"

def BLOODUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Running Bloodhound{RESET}")
    dc = input(f"{CYAN}DC IP (or name server IP): {RED} {RESET}")
    subprocess.call([f"bloodhound-python -ns {dc} -u {USER} -p {PASS} -d {DOMAIN} -c all"], shell=True)

def BLOODUH(DOMAIN, USER, HASH):
    print(f"{YELLOW}Running Bloodhound{RESET}")
    dc = input(f"{CYAN}DC IP (or name server IP): {RED} {RESET}")
    subprocess.call([f"bloodhound-python -ns {dc} -u {USER} --hashes :{HASH} -d {DOMAIN} -c all"], shell=True)    

def SMBN(DOMAIN):
    """Write owner over group with hashes"""
    print(f"{YELLOW}Enumerating target system with Null credentials on SMB{RESET}")
    subprocess.call([f"nxc smb {DOMAIN} {N} {ENUMSMB} | tee -a Null_SMB.txt"], shell=True)

def SMBUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Enumerating SMB target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and password {RED}{PASS}{RESET}")
    subprocess.call([f"nxc smb {DOMAIN} {UP} {ENUMSMB} | tee -a {USER}_{PASS}_SMB.txt"], shell=True)

def SMBUH(DOMAIN, USER, HASH):
    print(f"{YELLOW}Enumerating SMB target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc smb {DOMAIN} {UH} {ENUMSMB} | tee -a {USER}_{HASH}_SMB.txt"], shell=True)

def LDAPN(DOMAIN):
    print(f"{YELLOW}Enumerating target system with Null credentials on LDAP{RESET}")
    subprocess.call([f"nxc ldap {DOMAIN} {N} {ENUMLDAP} | tee -a Null_LDAP.txt"], shell=True)

def LDAPUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Enumerating LDAP target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc ldap {DOMAIN} {UP} {ENUMLDAP} | tee -a {USER}_{PASS}_LDAP.txt"], shell=True)

def LDAPUH(DOMAIN, USER, HASH):
    print(f"{YELLOW}Enumerating LDAP target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc ldap {DOMAIN} {UH} {ENUMLDAP} | tee -a {USER}_{HASH}_LDAP.txt"], shell=True)

def NFSN(DOMAIN):
    print(f"{YELLOW}Enumerating target system with Null credentials on NFS{RESET}")
    subprocess.call([f"nxc nfs {DOMAIN} {N} {ENUMNFS} | tee -a Null_NFS.txt"], shell=True)

def NFSUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Enumerating NFS target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc nfs {DOMAIN} {UP} {ENUMNFS} | tee -a {USER}_{PASS}_NFS.txt"], shell=True)

def FTPN(DOMAIN):
    print(f"{YELLOW}Enumerating target system with Null credentials on FTP{RESET}")
    subprocess.call([f"nxc ftp {DOMAIN} {N} {ENUMFTP} | tee -a Null_FTP.txt"], shell=True)

def FTPUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Enumerating FTP target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc ftp {DOMAIN} {UP} {ENUMFTP} | tee -a {USER}_{PASS}_FTP.txt"], shell=True)

def VNCN(DOMAIN):
    print(f"{YELLOW}Enumerating target system with Null credentials on VNC{RESET}")
    subprocess.call([f"nxc vnc {DOMAIN} {N} {ENUMVNC} | tee -a Null_VNC.txt"], shell=True)

def VNCUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Enumerating VNC target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc vnc {DOMAIN} {UP} {ENUMVNC} | tee -a {USER}_{PASS}_VNC.txt"], shell=True)

def WMIN(DOMAIN):
    print(f"{YELLOW}Enumerating target system with Null credentials on WMI{RESET}")
    subprocess.call([f"nxc wmi {DOMAIN} {N} | tee -a Null_WMI.txt"], shell=True)

def WMIUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Enumerating WMI target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc wmi {DOMAIN} {UP} | tee -a {USER}_{PASS}_WMI.txt"], shell=True)

def WMIUH(DOMAIN, USER, HASH):
    print(f"{YELLOW}Enumerating WMI target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc wmi {DOMAIN} {UH} | tee -a {USER}_{HASH}_WMI.txt"], shell=True)

def SSHUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Enumerating SSH target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc SSH {DOMAIN} {UP} | tee -a {USER}_{PASS}_SSH.txt"], shell=True)

def SSHUH(DOMAIN, USER, HASH):
    print(f"{YELLOW}Enumerating SSH target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc ssh {DOMAIN} {UH} | tee -a {USER}_{HASH}_SSH.txt"], shell=True)

def RDPUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Enumerating RDP target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc rdp {DOMAIN} {UP} | tee -a {USER}_{PASS}_RDP.txt"], shell=True)

def RDPUH(DOMAIN, USER, HASH):
    print(f"{YELLOW}Enumerating RDP target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    subprocess.call([f"nxc rdp {DOMAIN} {UH} | tee -a {USER}_{HASH}_RDP.txt"], shell=True)

def MSSQLUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Enumerating MSSQL target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    print(f"{YELLOW}Is using local user you will need to check for yourself{RESET}")
    subprocess.call([f"nxc mssql {DOMAIN} {UP} | tee -a {USER}_{PASS}_MSSQL.txt"], shell=True)

def MSSQLUH(DOMAIN, USER, HASH):
    print(f"{YELLOW}Enumerating MSSQL target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    print(f"{YELLOW}Is using local user you will need to check for yourself{RESET}")
    subprocess.call([f"nxc mssql {DOMAIN} {UH} | tee -a {USER}_{HASH}_MSSQL.txt"], shell=True)

def WINRMUP(DOMAIN, USER, PASS):
    print(f"{YELLOW}Enumerating WINRM target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    print(f"{YELLOW}Is using local user you will need to check for yourself{RESET}")
    subprocess.call([f"nxc winrm {DOMAIN} {UP} | tee -a {USER}_{PASS}_WINRM.txt"], shell=True)

def WINRMUH(DOMAIN, USER, HASH):
    print(f"{YELLOW}Enumerating WINRM target system on Domain {RED}{DOMAIN}{YELLOW} with user {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
    print(f"{YELLOW}Is using local user you will need to check for yourself{RESET}")
    subprocess.call([f"nxc winrm {DOMAIN} {UH} | tee -a {USER}_{HASH}_WINRM.txt"], shell=True)


def main():
    # Conditional checks for USER, PASS, HASH to handle appropriate functions
    if USER is None and PASS is None:
        # Call functions that don't require credentials
        SMBN(DOMAIN)
        LDAPN(DOMAIN)
        FTPN(DOMAIN)
        WMIN(DOMAIN)
        NFSN(DOMAIN)
        VNCN(DOMAIN)
    elif HASH:
        # Use the hash-based functions if HASH is provided
        BLOODUH(DOMAIN, USER, HASH)
        SMBUH(DOMAIN, USER, HASH)
        LDAPUH(DOMAIN, USER, HASH)
        WMIUH(DOMAIN, USER, HASH)
        MSSQLUH(DOMAIN, USER, HASH)
        WINRMUH(DOMAIN, USER, HASH)
        SSHUH(DOMAIN, USER, HASH)
        RDPUH(DOMAIN, USER, HASH)
    elif USER and PASS:
        # Use the username and password-based functions if both are provided
        BLOODUP(DOMAIN, USER, PASS)
        SMBUP(DOMAIN, USER, PASS)
        LDAPUP(DOMAIN, USER, PASS)
        WMIUP(DOMAIN, USER, PASS)
        VNCUP(DOMAIN, USER, PASS)
        FTPUP(DOMAIN, USER, PASS)
        NFSUP(DOMAIN, USER, PASS)
        MSSQLUP(DOMAIN, USER, PASS)
        WINRMUP(DOMAIN, USER, PASS)
        SSHUP(DOMAIN, USER, PASS)
        RDPUP(DOMAIN, USER, PASS)


if __name__ == '__main__':
    main()

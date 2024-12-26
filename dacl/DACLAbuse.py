#!/usr/bin/env python3

import os
import sys
import time
import subprocess
from time import sleep
import argparse
from subprocess import Popen

sys.path.append(os.path.join(os.path.dirname(__file__), 'dacltools'))


# Import other tools
from argument_parser import parse_arguments  # Import parse_arguments function
from targetedkerb import Targ, HTarg
from addmem import Ahash, Apass
from WriteOwner import WOpassG, WOpassU, WOhashU, WOhashG, whois
from WriteDACL import WriteDaclPass, WriteDaclHash, WriteDaclPassG, WriteDaclHashG, WriteDaclPassU, WriteDaclHashU
from GenericAll import GenericAllPass, GenericAllHash
from ForceChange import ForceChangeH, ForceChangeP
from Enumerate import BLOODUH, BLOODUP, SMBN, SMBUP, SMBUH, LDAPN, LDAPUP, LDAPUH, SSHUP, SSHUH, RDPUP, RDPUH, WMIN, WMIUP,WMIUH, VNCN, VNCUP, FTPN, FTPUP, NFSN, NFSUP, MSSQLUP, MSSQLUH, WINRMUP, WINRMUH
from dcsync import DCHash, DCPass
from GenericWrite import GWUP, GWGP, GWGH, GWUH

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

def main():
    # Parse arguments once here and make them globally accessible
    args = parse_arguments()

    # Extract arguments from the parsed `args` object
    DOMAIN = args.DomainName
    USER = args.Username
    PASS = args.Password
    HASH = args.PassTheHash
    TargetedKerberoast = args.TargetedKerberoast
    AddMembers = args.AddMembers
    WriteDacl = args.WriteDacl
    ForceChangePassword = args.ForceChangePassword
    WriteOwner = args.WriteOwner
    GenericAll = args.GenericAll
    GenericWrite = args.GenericWrite
    DCSync = args.DCSync
    
    if GenericWrite:
        who_choice = whois()
        if HASH:
            GWUH();GWGH()
        else:
            GWUP();GWGP()

    if TargetedKerberoast:
        if HASH:
            HTarg()  # If Pass-the-Hash is used, call HTarg
        else:
            Targ()  # Otherwise, call Targ
    
    if AddMembers:
        if HASH:
            Ahash()  # If Pass-the-Hash is used, call Ahash
        else:
            Apass()  # Otherwise, call Apass

    if WriteDacl:
        if HASH:
            WriteDaclHash()
        else:
            WriteDaclPass()  # Implement this function based on your needs

    if ForceChangePassword:
        ForceChangePassword()  # Implement this function based on your needs

    if WriteOwner:
        who_choice = whois()
        if HASH:
            if who_choice == "g":
                WOhashG(DOMAIN, USER, HASH)
            else:
                WOhashU(DOMAIN, USER, HASH)
        else:
            if who_choice == "g":
                WOpassG(DOMAIN, USER, PASS)
            else:
                WOpassU(DOMAIN, USER, PASS)
    
    if GenericAll: 
        if HASH:    
            GenericAllHash()
        else:
            GenericAllPass()

    if DCSync:
        if HASH:
            DCHash()
        else:
            DCPass()
    # Check for the -E flag (Enumerate with Null credentials)
    if args.Enumerate:
        print(f"{YELLOW}Enumerating target system on Domain {RED}{DOMAIN}{RESET} with Null credentials")
        SMBN(DOMAIN)  # SMB with Null credentials
        LDAPN(DOMAIN)  # LDAP with Null credentials
        FTPN(DOMAIN)  # FTP with Null credentials
        WMIN(DOMAIN)  # WMI with Null credentials
        NFSN(DOMAIN)  # NFS with Null credentials
        VNCN(DOMAIN)  # VNC with Null credentials
        if USER and PASS:
            print(f"{YELLOW}Enumerating target system with username {RED}{USER}{RESET} and password {RED}{PASS}{RESET}")
            BLOODUP(DOMAIN, USER, PASS)
            SMBUP(DOMAIN, USER, PASS)
            LDAPUP(DOMAIN, USER, PASS)
            FTPUP(DOMAIN, USER, PASS)
            WMIUP(DOMAIN, USER, PASS)
            NFSUP(DOMAIN, USER, PASS)
            VNCUP(DOMAIN, USER, PASS)
        elif HASH:
            print(f"{YELLOW}Enumerating target system with username {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
            BLOODUH(DOMAIN, USER, HASH)
            SMBUH(DOMAIN, USER, HASH)
            LDAPUH(DOMAIN, USER, HASH)
            WMIUH(DOMAIN, USER, HASH)
        else:
            print(f"{RED}Error: You need to provide either a username/password or a hash for enumeration!{RESET}")
            return  # Exit if no valid authentication method is provided

if __name__ == '__main__':
    main()

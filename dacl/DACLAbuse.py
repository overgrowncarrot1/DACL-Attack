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
from dacltools.WriteDACL import (whois_dacl, WriteDaclPass, WriteDaclHash,
    WriteDaclPassG, WriteDaclHashG, WriteDaclPassU, WriteDaclHashU)
from GenericAll import whois_GA, GenericAllPass, GenericAllHash, GenericAllPassC, GenericAllHashC, GenericAllHashG, GenericAllPassG
from ForceChange import ForceChangeH, ForceChangeP
from Enumerate import BLOODUH, BLOODUP, SMBN, SMBUP, SMBUH, LDAPN, LDAPUP, LDAPUH, SSHUP, SSHUH, RDPUP, RDPUH, WMIN, WMIUP,WMIUH, VNCN, VNCUP, FTPN, FTPUP, NFSN, NFSUP, MSSQLUP, MSSQLUH, WINRMUP, WINRMUH
from dcsync import DCHash, DCPass
from GenericWrite import whois_GW, GWUP, GWGP, GWGH, GWUH
from AddCredentialLink import ACLH, ACLP

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
    AddCredentialLink = args.AddCredentialLink
    
    if GenericWrite:
        who_choice = whois_GW()
        if HASH:
            if who_choice == 'g':
                GWGH()
            else:
                GWUH()
        else:
            if who_choice == 'g':
                GWGP()
            else:
                GWUP()

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
        who_choice = whois_dacl()
        if who_choice not in ['c', 'g', 'u']:
            print(f"{RED}Invalid input! Please choose 'c' 'g' or 'u'.")
            return 
        if HASH:
            if who_choice == 'g':
                WriteDaclHashG()
            elif who_choice == 'u':
                WriteDaclHashU()
            else:
                WriteDaclHash()
        else:
            if who_choice == 'g':
                WriteDaclPassG()  # Implement this function based on your needs
            elif who_choice == 'u':
                WriteDaclPassU()
            else:
                WriteDaclPass()

    if ForceChangePassword:
        if HASH:
            ForceChangeH()
        else:
            ForceChangeP()  # Implement this function based on your needs

    if WriteOwner:
        who_choice = whois()
        if HASH:
            if who_choice == "g":
                WOhashG()
            else:
                WOhashU()
        else:
            if who_choice == "g":
                WOpassG()
            else:
                WOpassU()
    
    if GenericAll: 
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

    if DCSync:
        if HASH:
            DCHash()
        else:
            DCPass()

    if AddCredentialLink:
        if HASH:
            ACLH()
        else:
            ACLP()

    # Check for the -E flag (Enumerate with Null credentials)
    if args.Enumerate:
        if USER == None and PASS == None:
            print(f"{YELLOW}Enumerating target system on Domain {RED}{DOMAIN}{RESET} with Null credentials")
            # Call functions that don't require credentials
            SMBN()
            LDAPN()
            FTPN()
            WMIN()
            NFSN()
            VNCN()
        if USER and PASS:
            print(f"{YELLOW}Enumerating target system with username {RED}{USER}{RESET} and password {RED}{PASS}{RESET}")
            BLOODUP()
            SMBUP()
            LDAPUP()
            FTPUP()
            WMIUP()
            NFSUP()
            VNCUP()
        if HASH:
            print(f"{YELLOW}Enumerating target system with username {RED}{USER}{RESET} and hash {RED}{HASH}{RESET}")
            BLOODUH()
            SMBUH()
            LDAPUH()
            WMIUH()
        else:
            print(f"{RED}Error: You need to provide either a username/password or a hash for enumeration!{RESET}")
            return  # Exit if no valid authentication method is provided

if __name__ == '__main__':
    main()

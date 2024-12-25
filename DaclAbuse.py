#!/usr/bin/env python3

import os
import sys
import time
import subprocess
from time import sleep
import argparse
from subprocess import Popen

# Import other tools
from argument_parser import parse_arguments  # Import parse_arguments function
from targetedkerb import Targ, HTarg
from addmem import Ahash, Apass
from WriteOwner import WOpassG, WOpassU, WOhashU, WOhashG, whois
from WriteDACL import WriteDaclPass, WriteDaclHash
from GenericAll import GenericAllPass, GenericAllHash
from ForceChange import ForceChangeH, ForceChangeP

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
    PasswordAbuse = args.PasswordAbuse
    WriteDacl = args.WriteDacl
    ForceChangePassword = args.ForceChangePassword
    WriteOwner = args.WriteOwner
    WriteDacl = args.WriteDacl
    GenericaAll = args.GenericAll
    
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

    if PasswordAbuse:
        PasswordAbuse()  # Implement this function based on your needs

    if WriteDacl:
        if HASH:
            WriteDaclHash()
        else:
            WriteDaclPass()  # Implement this function based on your needs

    if ForceChangePassword:
        ForceChangePassword()  # Implement this function based on your needs

    if WriteOwner:
        if HASH:
            WOhash()  # If Pass-the-Hash is used, call WOhash
        else:
            WOpass()  # Otherwise, call WOpass
            
    if GenericaAll:
        if HASH:
            GenericaAllHash()
        else:
            GenericaAllPass()

if __name__ == '__main__':
    main()

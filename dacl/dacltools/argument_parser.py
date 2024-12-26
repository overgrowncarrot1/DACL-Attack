#!/usr/bin/env python3

import argparse
import sys

def parse_arguments():
    # Argument parsing for different options
    parser = argparse.ArgumentParser(description="DACL Tool", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    # Define all the possible actions
    parser.add_argument("-T", "--TargetedKerberoast", action="store_true", help="Targeted Kerberoasting")
    parser.add_argument("-A", "--AddMembers", action="store_true", help="Add Members")
    parser.add_argument("-W", "--WriteDacl", action="store_true", help="Write DACL")
    parser.add_argument("-F", "--ForceChangePassword", action="store_true", help="Force Change Password")
    parser.add_argument("-G", "--GenericAll", action="store_true", help="Generic All Attack")
    parser.add_argument("-R", "--GenericWrite", action="store_true", help="Generic Write Attack")
    parser.add_argument("-D", "--DCSync", action="store_true", help="DCSync Attack")
    parser.add_argument("-O", "--WriteOwner", action="store_true", help="Write Owner")
    parser.add_argument("-d", "--DomainName", action="store", help="Domain Name", required=True)
    
    # Modify these lines to make username and password optional when -E is used
    parser.add_argument("-u", "--Username", action="store", help="Username")
    parser.add_argument("-p", "--Password", action="store", help="Password")
    
    parser.add_argument("-H", "--PassTheHash", action="store", help="Hash")
    parser.add_argument("-E", "--Enumerate", action="store_true", help="Enumerate the Target System with NetExec")
    
    args = parser.parse_args()  # Parse the arguments
    
    # If no arguments are passed or critical arguments are missing, show help
    if not any(vars(args).values()):  # Check if no arguments were provided
        parser.print_help()
        sys.exit(1)  # Exit the program after showing help
    
    # If not in enumerate mode, username and password are required
    if not args.Enumerate:
        if not args.Username or not args.Password:
            parser.print_help()
            sys.exit(1)  # Exit after showing the help if required arguments are missing
    
    return args  # Return the parsed arguments

# If you want to use this file standalone for debugging or testing
if __name__ == '__main__':
    args = parse_arguments()
    print(args)

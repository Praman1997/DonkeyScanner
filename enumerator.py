#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from geoip import geolite2
import os
import sys
import socket

def run():
    logo = """
 _____                                     _
|  ___|                                   | |
| |__ _ __  _   _ _ __ ___   ___ _ __ __ _| |_ ___  _ __
|  __| '_ \| | | | '_ ` _ \ / _ \ '__/ _` | __/ _ \| '__|
| |__| | | | |_| | | | | | |  __/ | | (_| | || (_) | |
\____/_| |_|\__,_|_| |_| |_|\___|_|  \__,_|\__\___/|_|
    """

    menu = """
[0] Go Back...
[1] Traceroute
[2] Ping Test
[3] DNS Lookup (Works only if you have 'dnsenum' pre-installed)
[4] Find DNS Host
[5] Find Shared DNS
[6] Zone Transfer
[7] Whois Lookup
[8] IP Location Lookup
[9] Reverse IP Lookup
[10] TCP Port Scan
[11] HTTP Header Check
    """
    print logo
    print menu
    try:
        choice = input("Which option number : ")

        if choice == 1:
            print("\n")
            print("[+] Traceroute script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            command = "traceroute "+target
            os.system(command)

        elif choice == 2:
            print("\n")
            print("[+] Ping Test script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            command = "ping -c 4 "+str(target)
            os.system(command)

        elif choice == 3:
            try:
                print("\n")
                print("[+] DNS Lookup script running..")
                target = raw_input("[+] Target : ")
                print("\n")
                command = "dnsenum -v "+str(target)
                os.system(command)
            except Exception as e:
                raise ("[-] You don't have 'dnsenum' pre-installed!")
                print ("[!] Please install 'dnsenum', if you want this option to work...")

        elif choice == 4:
            print("\n")
            print("[+] Find Host DNS script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            command = "host -v "+str(target)
            os.system(command)

        elif choice == 5:
            print("\n")
            print("[+] Find Shared DNS script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            command = "dnsrecon -wd "+str(target)
            os.system(command)

        elif choice == 6:
            print("\n")
            print("[+] Zone Transfer script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            command = "dnsrecon -d "+str(target)+ " -t axfr"
            os.system(command)

        elif choice == 7:
            print("\n")
            print("[+] Whois Lookup script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            command = "whois "+str(target)
            os.system(command)

        elif choice == 8:
            print("\n")
            print("[+] IP Location Lookup script running..")
            target = raw_input("[+] Target : ")
            match = geolite2.lookup(target)
            result = "[IPInfo] IP Address: "+str(match.ip)+"\n[IPInfo] Country: "+str(match.country)+"\n[IPInfo] Continent:"+str(match.continent)+"\n[IPInfo] Subdivision:"+str(match.subdivisions)+"\n[IPInfo] Timezone:"+str(match.timezone)+"\n[IPInfo] Location:"+str(match.location)
            print(result)

        elif choice == 9:
            print("\n")
            print("[+] Reverse IP Lookup script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            reversed_ip = socket.gethostbyaddr(target)
            print(str(reversed_ip[0]))

        elif choice == 10:
            print("\n")
            print("[+] TCP Port Scan script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            command = "sudo nmap -A -p- "+str(target)
            os.system(command)

        elif choice == 11:
            print("\n")
            print("[+] HTTP Header Check script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            request = requests.get(target)
            txt = request.headers
            print(str(txt))

        elif choice == 0:
            # This will go back to dscan... Probably!
            print("[!] Back to DonkeyScanner!")

        else:
            print("[-] Invalid Option!")
            run()

    except KeyboardInterrupt:
        print("\n[-] Aborted!")
        quit()

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] DonkeyScan installer must be run as root. ¯\_(ツ)_/¯\n\033[1;m""")

print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                     DonkeyScan Installer                     █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")

def main():

	print("\033[1;34m\n[++] Please choose your operating system.\033[1;m")

	print("""
1) Ubuntu / Kali linux / Others
2) Parrot OS
""")
	system0 = raw_input(">>> ")
	if system0 == "1":
		print("\033[1;34m\n[++] Installing DonkeyScan ... \033[1;m")
		install = os.system("sudo apt-get update && sudo apt-get install -y nmap build-essential python-pip ruby-dev git libpcap-dev libgmp3-dev && sudo pip install tabulate terminaltables")

		install1 = os.system("""sudo mkdir -p /opt/dscan && sudo cp -R tools/ /opt/dscan/ && sudo cp dscan.py /opt/dscan/dscan.py && sudo cp banner.py /opt/dscan/banner.py && sudo cp run.sh /usr/bin/dscan && sudo chmod +x /usr/bin/dscan && tput setaf 34; echo "DonkeyScan has been sucessfuly instaled. Execute 'dscan' in your terminal." """)	
	elif system0 == "2":
		print("\033[1;34m\n[++] Installing DonkeyScan ... \033[1;m")

		install = os.system("sudo apt-get update && sudo apt-get install -y nmap ruby-dev git libpcap-dev libgmp3-dev python-tabulate python-terminaltables")

		install1 = os.system("""sudo mkdir -p /opt/dscan && sudo cp -R tools/ /opt/dscan/ && sudo cp dscan.py /opt/dscan/dscan.py && sudo cp banner.py /opt/dscan/banner.py && sudo cp run.sh /usr/bin/dscan && sudo chmod +x /usr/bin/dscan && tput setaf 34; echo "DonkeyScan has been sucessfuly instaled. Execute 'dscan' in your terminal." """)
		

	else:
		print("Please select the option 1 or 2")
		main()
main()

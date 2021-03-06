#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports
import enumerator
import os, sys, traceback
import socket
import ipaddress as ip
from pathlib import Path
from terminaltables import DoubleTable
from tabulate import tabulate
from banner import xe_header
from time import sleep
#---------------------------------------------------------------
# Welcome screen and home screen in one
try:

	def home():
		# Configure the network interface and gateway...
		global up_interface
		up_interface = open('/opt/dscan/tools/files/iface.txt', 'r').read()
		up_interface = up_interface.replace("\n","")
		if up_interface == "0":
			up_interface = os.popen("route | awk '/Iface/{getline; print $8}'").read()
			up_interface = up_interface.replace("\n","")
			global gateway
		gateway = open('/opt/dscan/tools/files/gateway.txt', 'r').read()
		gateway = gateway.replace("\n","")
		if gateway == "0":
			gateway = os.popen("ip route show | grep -i 'default via'| awk '{print $3 }'").read()
		gateway = gateway.replace("\n","")
		n_name = os.popen('iwgetid -r').read() # Get wireless network name
		n_mac = os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read() # Get network mac
		n_ip = os.popen("hostname -I").read() # Local IP address
		n_host = os.popen("hostname").read() # hostname
			#-----------------------------------------------------------#
		if not os.geteuid() == 0:
			sys.exit("\n[!] DonkeyScanner must be run as root. ¯\_(ツ)_/¯ \n")
		author = "CR4CKB0X (9R4M4N K4SL1W4L)"
		print(xe_header())
		print ("\t\t\t\t\t\t A complete Network-MAP-per\n")
		print("Created By: "+author+"\nGit Account: https://github.com/Praman1997")
		print("--------------------------------------------------------------------------")
		print("\n\n")
		# Printing the network configuration
		table = [["IP Address","MAC Address","Gateway","Iface","Hostname"],
			 	["","","","",""],
			 	[n_ip,n_mac.upper(),gateway,up_interface,n_host]]
		table = DoubleTable(table)
		print (table.table)
		print("----------------------------\n\n")

	def options_list():
		option_table = [["Command","Explanation..."],
						["enum","Run ENUMERATOR!"],
						["getip","Get IP Address from URL (I honestly didn't think that was possible!)"],
						["make","List available IP Addresses (It's Basic, yo!)"],
						["ipscan","IP Scan or Subnet Scan (Beginners' Stuff)"],
						["idlescan","Idle or Zombie Scan ('WTF?!' Stuff)"],
						["evasion","IDS, IPS or Firewall Evasion ('I know what I am doing...' Stuff)"],
						["osscan","Operating System detection ('Woah!!! Magic!!!' Stuff)"],
						["help","Show this list at any point of time"],
						["banner","Show random banner (They are really cool...)"],
						["cls","Clear Screen"],
						["update","Update to current version of DonkeyScanner"],
						["exit","Whimp out and go home!"]]
		option_table = DoubleTable(option_table)
		print (option_table.table)

	def command():
		try:
			initial_choice = raw_input("dscan>> ")
		except KeyboardInterrupt as k:
			print ("\n[*] Keyboard Interrupt Detected!")
			command()
		
		if (initial_choice == "make"):
			try:
				make_list()
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "enum"):
			try:
				run_enum()
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "getip"):
			try:
				getIP()
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "ipscan"):
			try:
				ip_scan()
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "idlescan"):
			try:
				idle_scan()
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "evasion"):
			try:
				evasion()
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "osscan"):
			try:
				os_detection()
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "help"):
			try:
				options_list()
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "banner"):
			try:
				os.system("clear")
				home()
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "cls"):
			try:
				os.system("clear")
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "update"):
			try:
				update()
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()
		elif (initial_choice == "exit"):
			print ("[*] GoodBye!!!")
			exit(0)
		else:
			try:
				print ("Error 404: Command not found. Please try again!")
				sleep(1)
				print ("Note: Enter 'help' for command list...\n")
				sleep(1)
				command()
			except KeyboardInterrupt as k:
				print ("\n[*] Keyboard Interrupt Detected!")
				command()

	def update():
		os.system("clear")
		print ("[+] Updating DonkeyScanner! This may take a few minutes")
		try:
			os.system("git clone https://github.com/Praman1997/DonkeyScanner.git && cd DonkeyScanner && sudo python install.py && cd .. && sudo rm -rf DonkeyScanner/")
			print ("[+] DonkeyScanner updated successfully... Please restart using 'dscan' command as before...")
		except Exception as e:
			print ("[-] Error while updating the DonkeyScanner...\n[*] In order to do it manually, please type the following commands:")
			print ("[Step 1] git clone https://github.com/Praman1997/DonkeyScanner.git && cd DonkeyScanner")
			print ("[Step 2] sudo python install.py\n\t[*] Once prompted, select the appropriate option...")
			print ("[Step 3] cd .. && sudo rm -rf DonkeyScanner/")
			print ("[Step 4] sudo dscan")

	def make_list():
		os.system("clear")
		print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█              Listing Available IP Addresses                  █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")
		subnet = raw_input("\n\nEnter subnet (Eg: 192.168.0.*): ")
		command = "nmap -sn "+subnet+" | grep -o "+subnet+" > /opt/dscan/available_ip_addresses.txt "
		os.system(command)
		print ("List Complete...\n")
		show_list = raw_input("Do you want to see the list? (y/n): ")
		if (show_list == "y" or show_list == "Y"):
			os.system('echo "Showing the list:\n" && cat /opt/dscan/available_ip_addresses.txt')
			sleep (1)

	def run_enum():
		enumerator.run()
		sleep (5)

	def getIP():
		os.system("clear")
		print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█        		Get IP Address		               █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")
		url = raw_input("Enter URL: ")
		print (socket.gethostbyname(url))
		print ("Note: Copy the IP Address, I will wait for 5 seconds!")
		sleep(5)

	def ip_scan():
		os.system("clear")
		print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█        		The IP Scanner		               █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")
		address = raw_input("Enter IP or Subnet (Eg: 192.168.0.25 or 192.168.0.*): ")
		scan_type = raw_input("Agressive Scan (A) or Stealth Scan (S): ")
		if (scan_type == "A" or scan_type == "a"):
			command = "nmap -sT -sV -v "+address+" "
		elif (scan_type == "S" or scan_type == "s"):
			command = "nmap -sS -sV -v "+address+" "
		else:
			print ("Incorrect Choice!!! It was either 'A' or 'S'... Are you thick?!!\n")
			sleep(1)
		os.system(command)

	def idle_scan():
		os.system("clear")
		print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█              	       Idle or Zombie Scan                     █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")
		table = [["code","Scan Type"],
		 		 ["idle","Zombie Scan with unknown zombie (Specific Port) "],
		 	 	 ["zomb","Zombie Scan with known zombie (Specific Port)"],
		 	 	 ["IDLE","Zombie Scan with unknown zombie (Top 1000 ports)"],
		 	 	 ["ZOMB","Zombie Scan with known zombie (Top 1000 ports)"],
		 	 	 ["home","Go back to Home"]]
		print (tabulate(table, stralign="center",tablefmt="fancy_grid",headers="firstrow"))
		print ("")
		scan_type = raw_input("dscan/idlescan>> ")
		if (scan_type == "idle"):
			target = raw_input("Enter Target IP: ")
			port = raw_input("Enter Specific Port: ")
			make_list()
			file = open("/opt/dscan/available_ip_addresses.txt","r")
			print("----------------------------------------------------")
			for x in file.readline():
				command = "nmap -Pn -p "+port+" -sI "+file.readline().strip()+" "+target+" "
				print ("\nTarget: "+target+"\nZombie: "+file.readline().strip()+"\nPort: "+port+"\n")
				os.system(command)
				print("-------------------------------------------------------")
			file.close()
		elif (scan_type == "zomb"):
			target = raw_input("Enter Target IP: ")
			zombie = raw_input("Enter Zombie IP: ")
			port = raw_input("Enter Specific Port: ")
			command = "nmap -Pn -p"+port+" -sI "+zombie+" "+target+" "
			print ("[+] Starting Zombie Scan for:\nTarget: "+target+"\nZombie: "+zombie+"\nPort: "+port+"\n")
			os.system(command)
			print("----------------------------------------------------")
		elif (scan_type == "IDLE"):
			target = raw_input("Enter Target IP: ")
			make_list()
			file = open("/opt/dscan/available_ip_addresses.txt","r")
			print("----------------------------------------------------")
			for x in file.readline():
				command = "nmap -Pn -sI "+file.readline().strip()+" "+target+" "
				print ("\nTarget: "+target+"\nZombie: "+file.readline().strip()+"\n")
				os.system(command)
				print("-------------------------------------------------------")
			file.close()
		elif (scan_type == "ZOMB"):
			target = raw_input("Enter Target IP: ")
			zombie = raw_input("Enter Zombie IP: ")
			command = "nmap -Pn -sI "+zombie+" "+target+" "
			print ("[+] Starting Zombie Scan for:\nTarget: "+target+"\nZombie: "+zombie+"\n")
			os.system(command)
			print("----------------------------------------------------")
		elif (scan_type == "home"):
			print("\n\n")
			pass
		else:
			print ("Are you thick?! How was that even difficult?!")
			sleep (2)
			idle_scan()

	def evasion():
		os.system("clear")
		print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█              	  IDS/IPS/Firewall Evasion                     █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")
		target = raw_input("Enter Target: ")
		port = raw_input("Enter specific port: ")
		scantype = raw_input("Scan Type (tcp or udp): ")
		if (scantype == "tcp" or scantype == "TCP"):
			command = "nmap -p"+port+" --script firewall-bypass.nse "+target+" "
		elif (scantype == "udp" or scantype == "UDP"):
			command = "nmap -p"+port+" -sU --script firewall-bypass.nse "+target+" "
		else:
			print ("ThickHead!!! It was either tcp or udp... How difficult is that??!")
			sleep(2)
			evasion()
		os.system(command)

	def os_detection():
		os.system("clear")
		print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█              		   OS Detection Scan    	               █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")
		target = raw_input("Enter Target: ")
		command = "nmap -O -sX "+target+" "
		os.system(command)

except KeyboardInterrupt:
	print ("\n[!] Keyboard Interrupt detected!\n")
	print ("[-] DonkeyScanner Aborted!")

#-------------------------------------------------------------------------------------------
try:
	os.system("clear")
	home()
	options_list()
	command()
except KeyboardInterrupt as k:
	print ("\n[*] Keyboard Interrupt Detected!")
	command()

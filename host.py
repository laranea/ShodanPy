import shodan
from authenticate import shodan_py
import ipaddr
import sys
import os
import socket

def host():
	while True:
		usr_inp=raw_input("host>>>")
		
		if usr_inp=="":
			usr_inp=raw_input("host>>>")

		elif usr_inp=="back":
			return

		elif usr_inp=="clear":
			os.system("clear")

		elif usr_inp=="quit" or usr_inp=="exit":
			quit()

		else:
			try:
    				socket.inet_aton(usr_inp)
				host_data=shodan_py.host(usr_inp)
				print("\n\n\n\n")
				print("IP Address: " +str(host_data['ip_str']))
				print("Organisation: " + str(host_data['org']))
				print("Country: " + str(host_data['country_name']))
				print("City: "+ str(host_data['city']))
				print("Region: " + str(host_data['region_code']))
				print("ASN: "+ str(host_data['asn']))
				print("Hostnames: " + str(host_data['hostnames']))
				print("Latitude: " + str(host_data['latitude']))
				print("Longitude: " + str(host_data['longitude']))
				print("Last Updated: " + str(host_data['last_update']))
				print("Ports used: " + str(host_data['ports']))
				print("OS: " + str(host_data['os']))
				print("\n\n\n")

			except socket.error:
   				print 'address/netmask is invalid:'
   				print 'Usage :host>>> <ip>'
				host()

import shodan
from authenticate import shodan_py
import os

def search():
	while True:
		usr_inp=raw_input("search>>>")

		if usr_inp=="":
			usr_inp==("search>>>")
		
		elif usr_inp=="clear":
			os.system("clear")

		elif usr_inp=="quit" or usr_inp=="exit":
			quit()

		elif usr_inp=="back":
			return

		else:	
			srch=shodan_py.search(usr_inp)
			print("Total Results: " + str(srch['total']))
			print("\n\n")
			for src in srch['matches']:
				print('IP: ' + str(src['ip_str']))
				print('OS: ' + str(src['os']))
				print('Hostnames: ' + str(src['hostnames']))
				print('Ports: ' + str(src['port']))
				print(str(src['data']))
					 	

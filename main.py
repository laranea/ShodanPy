#! usr/bin/python

import shodan
import os
import json
import sys
from ports import ports
from protocols import protocols
from search import search
from host import host
from count import count
from exploits import exploits
from help import help
import authenticate
from user_info import info

def main():

	while True:
		usr_inp=raw_input(">>>")

		if usr_inp=="":
			main()

		elif usr_inp=="search":
			search()
		
		elif usr_inp=="host":
			host()

		elif usr_inp=="ports":
			ports()

		elif usr_inp=="help":
			help()

		elif usr_inp=="count":
			count()

		elif usr_inp=="exploits":
			exploits()
	
		elif usr_inp=="hosts":
			hosts()

		elif usr_inp=="protocols":
			protocols()

		elif usr_inp=="info":
			info()

		elif usr_inp=="exit" or usr_inp=="quit":
			quit()

		elif usr_inp=="clear":
			os.system("clear")

		else:
			print("shodan_py: "+ usr_inp +" command not recognised")
			main()

help()
main()	

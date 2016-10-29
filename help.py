import shodan
from authenticate import shodan_py
import os
from banner import banner

def help():

	banner()
	print("""

		Author:vduddu
		Mail:vduddu@protonmail.com


		help: gives a list of all commands that can be used in the program

		host: takes IP Address as input and gives a list of information regarding the IP address

		search: allows users to search for strings withh detailed information of the query		 
		
		info: gives user account information

		ports: gives a list of all the ports that are searched by shodan

		protocols: gives a list of all the protocols that are searched by shodan

		count: gives a numerical result for a given query along with statistical data

		exploits: allows users to get information about different exploits

		back: moves out of sub-function to the main command line

		clear: clears the screen

		exit/quit: exits the program

		""")

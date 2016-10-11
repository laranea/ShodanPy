import shodan
from authenticate import shodan_py
import os

def count():
	
	#set=10
	
	FACETS={
	'org',
	'domain',
	'port',
	'asn',
	('country',5),
	}
	
	FACET_TITLE={
	'org' : 'Top 10 organisations',
	'domain' : 'Top 10 domains',
	'port' : 'Top 10 ports' ,
	'asn' : 'Top 10 asn' ,
	'country': 'Top 5 countries' ,
	}

	while True:
		usr_inp=raw_input("count>>>")
		
		if usr_inp=="back":
			return
	
		elif usr_inp=="exit" or usr_inp=="quit":
			quit()
		
		elif usr_inp=="":
			usr_inp=raw_input("count>>>")
		
		elif usr_inp=="clear":
			os.system("clear")

		else:
			try:
				cnt=shodan_py.count(usr_inp,facets=FACETS)
				print("Shodan Summary Information")
				print("\n\n")
				print("Total results:" + cnt['total'])
				for facet in cnt['facets']:
					print FACET_TITLES[facet]
					for term in cnt['facets'][facet]:
						print '%s: %s' % (term['value'], term['count'])
					print("\n")		
			except:
				print("Could not get information. Please try Again!!")
				print("Usage: <query>")
				print("To set default facets: set <number>")
				count()	

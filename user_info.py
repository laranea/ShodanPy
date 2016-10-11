import shodan
import json
from authenticate import shodan_py

def info():
	inf=shodan_py.info()
	print("Query Credits:\t" + str(inf['query_credits']))
	print("Credits Left:\t" + str(inf['unlocked_left']))
	print("Scan Credits:\t" + str(inf['scan_credits']))
	print("Account Plan:\t" + str(inf['plan']))

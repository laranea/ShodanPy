import shodan
from authenticate import shodan_py

def protocols():
	protocol=shodan_py.protocols()
	proto=[]
	for x in protocol:
		proto.append(x)
	for x in proto:
		print x

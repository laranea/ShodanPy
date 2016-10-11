import shodan
from authenticate import shodan_py 

def ports():
	prts=shodan_py.ports()
	split = len(prts)/4
	cols = 4
	split=[prts[i:i+len(prts)/cols] for i in range(0,len(prts),len(prts)/cols)]
	for row in zip(*split):
		print "".join(str.ljust(str(i),20) for i in row)

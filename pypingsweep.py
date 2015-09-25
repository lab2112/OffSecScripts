#!/usr/bin/python
#TODO: multithread so no delay
import subprocess, shlex

def pingit(ip):
	p1 = subprocess.Popen(['ping', '-c 1', ip], stdout=subprocess.PIPE)
	out = p1.communicate()[0]
	#print out
	if "bytes from" in out:
		print ip

def main():
	#pingit('192.168.1.200')
	for x in range(1,20):
		#print "Pinging ." + str(x)
		pingit('192.168.1.' + str(x))

if __name__=="__main__":
	main()
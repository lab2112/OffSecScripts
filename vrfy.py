#!/usr/bin/python
import socket
import sys

def verify_test(ip, user, out):
	#Create socket
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#Connect to the server
	connect = s.connect((ip, 25))

	#Receive the banner
	banner = s.recv(1024)

	print banner
	out.write("~~~~~" + user.strip() + "@" + ip.strip() + "~~~~~\n")
	out.write("Banner: " + banner)

	#VRFY a user
	s.send('VRFY ' + user.strip() + '\r\n')
	result = s.recv(1024)
	print result
	out.write("Result: " + result)
	
	#close socket
	s.close()

if len(sys.argv) !=3:
	print "Usage: vrfy.py <ip file> <user file>"
	sys.exit(0)
ips = open(sys.argv[1], 'r')
users = open(sys.argv[2], 'r')
outfile = open('smtpauto.out','a')
ip_list=[]
user_list=[]
for i in ips:
	ip_list.append(i)
for us in users:
	user_list.append(us)

for ip in ip_list:
	for user in user_list:
		print "trying " + user.strip() + "@" + ip.strip() 
		verify_test(ip, user, outfile)

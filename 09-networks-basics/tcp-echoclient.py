#!/usr/bin/python
#simple tcp echo client

import socket,sys

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost', 5090))
while True:
	data=raw_input("Enter data to send to server: press q or Q to quit:\n")
	c.send(data)
	if data=='q' or data=='Q':
		c.close()
		break
	print c.recv(512)

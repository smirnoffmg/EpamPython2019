#!/usr/bin/python
#UDP echo Server
import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('localhost',5000))
print "UDP -Echo Server listening on port 5000:"
while True:
	data,address=server_socket.recvfrom(512)
	print address, ":said", data
	server_socket.sendto(data,address)

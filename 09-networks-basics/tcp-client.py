#!/usr/bin/env python

from socket import *
s = socket(AF_INET,SOCK_STREAM)
<<<<<<< HEAD

s.connect(("localhost",50000))        # Connect
s.send(b"GET / HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")  # Send request
data = s.recv(10000)                    # Get response
s.close()
print(data)
=======
s.connect(("httpbin.org",80))        # Connect
s.send("GET / HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")  # Send request
data = s.recv(10000)                    # Get response
s.close()
print data
>>>>>>> upsteam/master

#http://httpbin.org

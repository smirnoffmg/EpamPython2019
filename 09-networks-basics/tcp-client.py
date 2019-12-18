#!/usr/bin/env python

from socket import *
s = socket(AF_INET,SOCK_STREAM)

s.connect(("localhost",50000))        # Connect
s.send(b"GET / HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")  # Send request
data = s.recv(10000)                    # Get response
s.close()
print(data)

#http://httpbin.org

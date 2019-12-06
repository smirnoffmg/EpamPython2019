#!/usr/bin/env python

from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",9000))
s.listen(5)
while True:
        c,a = s.accept()
        print "Received connection from", a
        c.send("Hello %s\n" % a[0])
        c.close()

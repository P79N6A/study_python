#!/usr/bin/env python
#
#
#

def printCharFromUnicode(u):
    uc = unicode()
    print "Char(UTF-8) is : %s" %(uc).decode('utf-8')


printCharFromUnicode(raw_input("Hello, Please input Unicode :"))
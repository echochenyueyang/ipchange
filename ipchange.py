#!/usr/bin/env python
import IPy
import re

file = open ("./ip.txt")

for line  in file:

    a = line
    a= line.split(' ')
   # print a[1],a[2]
    ip = IPy.IP(a[0])
    for x in ip:
        print x#,a[1],a[2]

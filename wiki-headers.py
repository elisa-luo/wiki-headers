#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:21:08 2020
wiki-headers
@author: elisaluo
"""
source = "test.txt" #filename of database

headers = []

data = open(source, 'r')

for line in data:
    if "==" in line:
        begin = line.find("==")
        end = line.rfind("==")
        head = line[begin+2:end]
        print ("["+head+"]")
        try:
            if not head[0] == '=': #get rid of subheaders
                headers.append(head)
        except IndexError:
            pass
        
            
            
    
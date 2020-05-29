#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:21:08 2020
wiki-headers
@author: elisaluo
"""
source = "wiki_data.txt" #filename of database

headers = []
word2count = {}

data = open(source, 'r')

for line in data:
    if "==" in line:
        begin = line.find("==")
        end = line.rfind("==")
        head = line[begin+2:end]
        #print ("["+head+"]")
        try:
            if not head[0] == '=': #exclude subheaders
                head = head.strip(' []')
                headers.append(head)
                words = head.split()
                #add to count dictionary
                for w in words:
                    if w not in word2count:
                        word2count[w] = 1;
                    elif w in word2count:
                        word2count[w] += 1;
        except IndexError:
            pass
        
#get most common words
rank = []
for word in word2count:
    rank.append((word2count[word], word))
rank.sort()

print(rank[-10:])
        
            
            
    
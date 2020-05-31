#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:21:08 2020
wiki-headers
@author: elisaluo
"""
source = "wiki_data.txt" #filename of dataset

#headers = []
word2count = {}

data = open(source, 'r')

### parse the data ###
for line in data:
    if "==" in line:
        begin = line.find("==")
        end = line.rfind("==")
        head = line[begin+2:end]
        #print ("["+head+"]")
        try:
            if not head[0] == '=': #exclude subheaders
                head = head.strip(' []') #get rid of extra characters/spaces
                #headers.append(head)
                words = head.split()
                ### add to count dictionary ###
                for w in words:
                    if w not in word2count:
                        word2count[w] = 1;
                    elif w in word2count:
                        word2count[w] += 1;
        except IndexError:
            pass
        
### get most common words ###
rank = []
for word in word2count:
    rank.append((word2count[word], word))
rank.sort()

### display top occurences ###
OCCURENCES =  10
top = rank[-OCCURENCES:]
top.reverse()

print("{} most common words in headers:\n".format(OCCURENCES))
print("{}COUNT\n{}".format("WORD".ljust(15),"-"*20))
for entry in top:
    count = entry[0]
    word = entry[1]
    print("{}{}".format(word.ljust(15),count))
        
            
            
    
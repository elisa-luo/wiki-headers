#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:21:08 2020
wiki-headers
@author: elisaluo
"""
import time
start_time = time.time()

### SETTINGS ###
SOURCE = "wiki_data.txt" #filename of dataset
OCCURENCES =  10 #<OCCURENCES> most common words to display
RUNTIME = True #display runtime
SUBHEADERS = False #include subheaders in rank
CASE_SENSITIVE = False


word2count = {}
data = open(SOURCE, 'r')

### read and clean-up the data ###
for line in data:
    if "==" in line and line[0] != '*': #exclude 'comment' lines beginning with *
        begin = line.find("==")
        end = line.rfind("==")
        head = line[begin+2:end]
        try:
            if SUBHEADERS:
                head = head.strip(' []=') #get rid of extra characters/spaces
                words = head.split()
                ### add to count dictionary ###
                for w in words:
                    if not CASE_SENSITIVE:
                        w = w.lower()
                    if w not in word2count:
                        word2count[w] = 1;
                    elif w in word2count:
                        word2count[w] += 1;    
            elif not SUBHEADERS:
                if not head[0] == '=': #exclude subheaders
                    head = head.strip(' []') #get rid of extra characters/spaces
                    words = head.split()
                    ### add to count dictionary ###
                    for w in words:
                        if not CASE_SENSITIVE:
                            w = w.lower()
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
top = rank[-OCCURENCES:]
top.reverse()

print("{} most common words in headers:".format(OCCURENCES))
print("CASE_SENSITIVE = {}".format(CASE_SENSITIVE))
print("INCLUDE SUBHEADERS = {}\n".format(SUBHEADERS))

print("{}{}COUNT\n{}".format("RANK ","WORD".ljust(15),"-"*25))
i = 1
for entry in top:
    count = entry[0]
    word = entry[1]
    print("{} {}{}".format((str(i)+". ").ljust(4),word.ljust(15),count))
    i+=1

### display total program runtime ###
if RUNTIME:    
    print("\n--- runtime: {} seconds ---".format(time.time() - start_time))
            
            
    
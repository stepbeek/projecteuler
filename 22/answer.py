#!/usr/bin/env python2
# Solution to project euler problem 22

translate = {'A': 1,'B': 2,'C': 3,'D': 4,'E': 5,'F': 6,'G': 7,'H': 8,'I': 9,'J': 10,'K': 11,'L': 12,'M': 13,'N': 14,'O': 15,'P': 16,'Q': 17,'R': 18,'S': 19,'T': 20,'U': 21,'V': 22,'W': 23,'X': 24,'Y': 25,'Z': 26}

def getnames(fname):
    lst = []
    with open(fname, 'r') as file:
        for line in file.readlines():
            lst.extend(line.split(","))
        for i in xrange(len(lst)):
            lst[i] = lst[i][1:-1]
        lst.sort()
    return lst

def calcnameval(s):
    val = 0
    for c in s:
        val += translate[c]
    return val

def solution():
    lst = getnames("./f.txt")
    total = 0
    for i in xrange(len(lst)):
        print lst[i]
        total += (i+1) * calcnameval(lst[i])
    return total

print solution()
        

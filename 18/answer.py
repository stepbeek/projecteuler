#!/usr/bin/env python2
# Solution to project euler problem 18

def readpyr(fname):
    ret = []
    with open(fname, 'r') as file:
        for line in file.readlines():
            nw = []
            for n in line.split(" "):
               nw.append(int(n))
            ret.append(nw)
    return ret

def collapserow(r):
    nw = []
    for i in xrange(1, len(r)):
        if r[i] > r[i-1]:
            nw.append(r[i])
        else:
            nw.append(r[i-1])
    return nw if nw != [] else r

def sumrows(r, s):
    ans = []
    for i in xrange(len(r)):
        ans.append(r[i] + s[i])
    return ans

def findmax(pyr):
    cpy = list(pyr)
    for i in range(len(pyr))[::-1]:
        if i + 1 < len(pyr):
            cpy[i] = sumrows(cpy[i], cpy[i+1])
            del cpy[i+1]
        cpy[i] = collapserow(cpy[i])
    return cpy

pyr = readpyr("./67.txt")
print findmax(pyr)

#!/usr/bin/env python2
# Solution to project euler problem 14

def collatzlength(start):
    x = start
    cnt = 0
    while x != 1:
        x = nextcollatz(x)
        cnt += 1
    return cnt
        
def nextcollatz(x):
    if x % 2 == 0:
        return x/2
    else:
        return 3*x + 1
    
def solution(n):
    mx = (0,0)
    for i in xrange(2, n + 1):
        ln = collatzlength(i)
        if ln > mx[1]:
            mx = (i, ln)
            print mx
    return mx

solution(1000000)

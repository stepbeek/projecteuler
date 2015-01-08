#!/usr/bin/env python2
# Solution to project euler problem 21
from sets import Set

sol = dict()

def findamicable(n):
    ans = Set()
    for i in xrange(1, n):
        if d(d(i)) == i and d(i) != i:
            ans.add(i)
            ans.add(d(i))
    return ans

def d(n):
    if n not in sol:
        sol[n] = sumdivisors(n)
    return sol[n]

def sumdivisors(n):
    ans = 0
    for i in xrange(1, n):
        if n % i == 0:
            ans += i
    return ans



print reduce(lambda x,y: x+y, findamicable(10000))

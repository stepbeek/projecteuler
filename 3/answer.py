#!/usr/bin/env python2
from math import sqrt

def genprimes(n):
    primes = sieve(n)
    answer = [y for y in xrange(2, n+1) if primes[y] == 1]

    return answer

def sieve(n):
    primes = [1]*(n+1)
    primes[0] = 0
    primes[1] = 0

    for i in xrange(2, n+1):
        if primes[i] == 1:
            x = i*i
            inc = 2 if i != 2 else 1
            while x <= n:
                primes[x] = 0
                x += inc*i
    return primes

def factorise(x):
    factors = []
    primes = genprimes(int(sqrt(x)) + 1)
    for i in primes:
        if x % i == 0:
            factors.append(i)
    return factors

print max(factorise(600851475143))

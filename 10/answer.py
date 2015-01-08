#!/usr/bin/env python2

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

print reduce(lambda x,y: x + y, genprimes(2000000))

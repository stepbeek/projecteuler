#!/usr/bin/env python2
# Solution to project euler problem 15

import itertools

from math import factorial as fac

def num_paths(m, n):
    return fac(m + n) / (fac(m) * fac(n))

print "m: %d, n: %d, number of paths: %d" % (20, 20, num_paths(20, 20))



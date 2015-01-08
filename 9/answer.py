#!/usr/bin/env python2
import math


def gensquares(ubnd):
    return map(lambda x: x**2, xrange(1, ubnd))

def gettriplet(ubnd):
    sqrs = gensquares(1000)
    for x in xrange(1, ubnd):
        y = 1
        while x + y < ubnd:
            zsqr = x**2 + y**2
            if zsqr in sqrs:
                yield x, y, math.sqrt(zsqr)
            y += 1



for x, y, z in gettriplet(1000):
    if 999 < x + y + z < 1001:
        print "x: %d, y: %d, z: %d\n" % (x,y,z)
        break
        

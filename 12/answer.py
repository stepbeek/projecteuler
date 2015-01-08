#!/usr/bin/env python2
# Solution to problem 12 from project euler
import unittest
from math import sqrt

def calctrianglenumber(n):
    """
    Calculates the nth triangle number.
    """
    return int((float(n * (n + 1)))/2)

def countdivisors(n):
    """
    Returns the count of the number of divisors of n.
    """
    res = 0
    for x in xrange(1, int(sqrt(n)) + 1):
        if n % x == 0:
           res += 1
    res *= 2
    sqr = sqrt(n)
    if int(sqr) == sqr:
        res -= 1
    return res


class Tests (unittest.TestCase):
    def test_calctrianglenumber(self):
        trianglenumbers = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

        for i in xrange(len(trianglenumbers)):
            self.assertEqual(calctrianglenumber(i+1), trianglenumbers[i])

    def test_countdivisors(self):
        self.assertEqual(countdivisors(10), 4)
        self.assertEqual(countdivisors(13), 2)
        self.assertEqual(countdivisors(100), 9)
        self.assertEqual(countdivisors(99), 6)
        

#unittest.main()


for i in xrange(100000000):
    if i % 1000 == 0:
        print i
    if countdivisors(calctrianglenumber(i)) >= 500:
        print "i: %d, solution: %d" % (i, calctrianglenumber(i))
        break
    

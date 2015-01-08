#!/usr/bin/env python2
# Solution to problem 16 of project euler
import unittest

def sumdigits(n):
    x = str(n)
    res = 0
    for c in x:
        res += int(c)
    return res

class Tests (unittest.TestCase):
    def test_sumdigits(self):
        self.assertEqual(10, sumdigits(1234))
        self.assertEqual(0, sumdigits(0))
        self.assertEqual(7, sumdigits(2**4))
        self.assertEqual(3, sumdigits(10011))
        self.assertEqual(9, sumdigits("2007"))

#unittest.main()

print sumdigits(2**1000)

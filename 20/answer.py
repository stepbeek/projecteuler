#!/usr/bin/env python2
# solution to project euler problem 20
import unittest

def factorial(n):
    fact = 1
    for i in xrange(1, n + 1):
        fact *= i
    return fact

def sumofdigits(n):
    s = str(n)
    total = 0
    for c in s:
        total += int(c)
    return total

def solution(n):
    return sumofdigits(factorial(n))

class Test (unittest.TestCase):
    def test_sumofdigits(self):
        self.assertEqual(6, sumofdigits(105))
        self.assertEqual(15, sumofdigits(12345))
        self.assertEqual(1, sumofdigits(1))
        self.assertEqual(0, sumofdigits(""))
        self.assertEqual(27, sumofdigits(3628800))

    def test_factorial(self):
        self.assertEqual(6, factorial(3))
        self.assertEqual(3628800, factorial(10))
        self.assertEqual(24, factorial(4))

#unittest.main()

print solution(100)

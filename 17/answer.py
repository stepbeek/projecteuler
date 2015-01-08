#!/usr/bin/env python2
# Solution to project euler problem 17

import unittest

transdict = {1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
             11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
             19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

def numtostring(n):
    if n > 1000:
        return ""
    elif n == 1000:
        return "one thousand"
    else:
        ans = ""
        x = n
        if 100 <= x <= 999:
            hndrs = int(x/100)
            x -= hndrs*100
            ans += transdict[hndrs]
            ans += " hundred"
            if x != 0:
                ans += " and "
            else:
                return ans
                
        if 11 <= x <= 19:
            ans += transdict[x]
            return ans
        elif 20 <= x <= 99:
            tens = int(x/10)*10
            x -= tens
            ans += transdict[tens] + " "
        if 1 <= x <= 10:
            ans += transdict[x]
        return ans

def countchars(s):
    cnt = 0
    dctnry = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']
    for c in s:
        if c in dctnry:
            cnt += 1
    return cnt

def solution():
    cnt = 0
    for i in xrange(1, 1001):
        print "%d: %s, count: %d" % (i, numtostring(i), countchars(numtostring(i)))
        cnt += countchars(numtostring(i))
    return cnt
    
class Tests (unittest.TestCase):
    def test_numtostring(self):
        self.assertEqual("one hundred and twenty six", numtostring(126))
        self.assertEqual("eleven", numtostring(11))
        self.assertEqual("nine hundred and ninety nine", numtostring(999))
        self.assertEqual("two hundred and two", numtostring(202))
        self.assertEqual("seven", numtostring(7))
        self.assertEqual("one hundred", numtostring(100))
        self.assertEqual("six hundred and ten", numtostring(610))

    def test_countchars(self):
        self.assertEqual(36, countchars("the quick brown fox jumped over the lazy dog"))
        self.assertEqual(10, countchars("hello world"))
        self.assertEqual(26, countchars("a b c d e f g h i j k l m n o p q r s t u v w x y z"))


#unittest.main()
print solution()


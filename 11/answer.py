#!/usr/bin/env python2
# Solution to project Euler problem 11
import unittest

grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
[04, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
[04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
[01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

def mh(arr, n):
    """
    Takes in a list and yields the products of n adjacent elements, cycling through the elements.
    """
    sze = len(arr)
    if sze >= n:
        x = 0
        while x + n <= sze:
            yield reduce(lambda x,y: x*y, arr[x : x + n])
            x += 1

def blankgen():
    for x in []:
        yield x 
            
def multhorz(arr, n):
    """
    Takes in a 2-d array and multiplies n elements at a time horizontally on each row.
    """
    for x in arr:
        for ans in mh(x, n):
            yield ans
            
def multvert(arr, n):
    """
    Takes in a 2-d array and multiplies vertically across arrays.
    """
    sze = len(arr[0])
    for i in xrange(sze):
        wl = []
        wl = [x[i] for x in arr]
        for ans in mh(wl, n):
            yield ans
    
def multdiagford(arr, n):
    """
    Takes in a  2-d array and generates the products of consecutive elements diagonally as a /.
    """
    sze = len(arr[0])
    num = len(arr)

    for i in xrange(n - 1, sze):
        for ans in fordiagproc(arr, 0, i, n):
            yield ans
            
    for i in xrange(1, num):
        for ans in fordiagproc(arr, i, sze - 1, n):
            yield ans


def fordiagproc(arr, x, y, n):
    sze = len(arr[0])
    num = len(arr)
    res = []
    while x < num and y >= 0:
        res.append(arr[x][y])
        x += 1
        y -= 1
        
    if len(res) >= n:
        return mh(res, n)
    else:
        return blankgen()

        
def multdiagback(arr, n):
    """
    Takes in a  2-d array and generates the products of consecutive elements diagonally as a /.
    """
    sze = len(arr[0])
    num = len(arr)
    for i in xrange(sze - n + 1):
        for ans in backdiagproc(arr, 0, i, n):
                yield ans

    for i in xrange(1, num):
        for ans in backdiagproc(arr, i, 0, n):
            yield ans

def backdiagproc(arr, x, y, n):
    sze = len(arr[0])
    num = len(arr)
    res = []
    while x < num and y < sze:
        res.append(arr[x][y])
        x += 1
        y += 1
        
    if len(res) >= n:
        return mh(res, n)
    else:
        return blankgen()

def solution(arr, n):
    ans = 0
    methods = [multhorz, multdiagford, multdiagback, multvert]
    for method in methods:
        for res in method(arr, n):
            if res > ans:
                ans = res
    return ans
    
class Tests (unittest.TestCase):
    def test_mh(self):
        res = [i for i in mh([1,2,3,4,5,6,7,8,9,10], 2)]
        self.assertEqual(res[0], 2)
        self.assertEqual(res[1], 6)
        self.assertEqual(res[2], 12)
        self.assertEqual(res[3], 20)
        self.assertEqual(res[4], 30)
        self.assertEqual(res[5], 42)
        self.assertEqual(res[6], 56)
        self.assertEqual(res[7], 72)
        self.assertEqual(res[8], 90)

    def test_multhorz(self):
        res = [i for i in multhorz([[1,2,3,4,5], [6,7,8,9,10]], 2)]
        self.assertEqual(res[0], 2)
        self.assertEqual(res[1], 6)
        self.assertEqual(res[2], 12)
        self.assertEqual(res[3], 20)
        self.assertEqual(res[4], 42)
        self.assertEqual(res[5], 56)
        self.assertEqual(res[6], 72)
        self.assertEqual(res[7], 90)

    def test_multvert(self):
        res = [i for i in multvert([[1,2,3], [4,5,6], [7,8,9]], 2)]
        self.assertEqual(res[0], 4)
        self.assertEqual(res[1], 28)
        self.assertEqual(res[2], 10)
        self.assertEqual(res[3], 40)
        self.assertEqual(res[4], 18)
        self.assertEqual(res[5], 54)
        
    def test_multdiagford(self):
        res = [i for i in multdiagford([[1,2,3], [4,5,6], [7,8,9]], 2)]
        self.assertEqual(res[0], 8)
        self.assertEqual(res[1], 15)
        self.assertEqual(res[2], 35)
        self.assertEqual(res[3], 48)

    def test_multdiagback(self):
        res = [i for i in multdiagback([[1,2,3], [4,5,6], [7,8,9]], 2)]
        self.assertEqual(res[0], 5)
        self.assertEqual(res[1], 45)
        self.assertEqual(res[2], 12)
        self.assertEqual(res[3], 32)


#unittest.main()

print "Solving euler problem 11...\n"
print "Answer: %d" % solution(grid, 4)



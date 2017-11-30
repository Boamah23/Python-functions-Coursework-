import unittest

def armstrong(n, r):
    sum = 0 #initialise sum with 0
    m = n #temporary value equals current value
    while m!=0:
        placeValue = m % 10 #finds a units value
        sum = sum + (placeValue**3) #cubes value and adds it to sum
        m = m // 10 #discards values unit m is 0 
    if(sum == n):
        return True
    else:
        return False

class armstrongTest(unittest.TestCase):

    def testOne(self):
        self.assertTrue(armstrong(153, (1**3 + 5**3 + 3**3)))

    def testTwo(self):
        self.assertFalse(armstrong(154, (1**3 + 5**3 + 4**3)))

def main():
    unittest.main()

if __name__ == '__main__':
    main()

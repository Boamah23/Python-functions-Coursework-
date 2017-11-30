import unittest
def readReverse(n):
    i = n.find(' ')  #finds spaces in input
    if i == -1:  #checks if there are no spaces
        return n[::-1] #reverses input
    else:  
        return n[:i][::-1] + ' ' + readReverse(n[i+1:]) #splits first word and reverses then second etc.

class readReverseTests(unittest.TestCase):

    def testOne(self):
        s = (readReverse("computer"))
        self.assertEqual(s, "retupmoc")
    def testTwo(self):
        s = (readReverse("computer science"))
        self.assertEqual(s, "retupmoc ecneics")
    def testThree(self):
        s = (readReverse("computer"))
        self.assertNotEqual(s, "computer")
    def testFour(self):
        s = (readReverse("computer science"))
        self.assertNotEqual(s, "computer science")
    

def main():
    unittest.main()

if __name__ == '__main__':
    main()

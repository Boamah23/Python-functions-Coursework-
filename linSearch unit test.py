import unittest

def linSearch(list, target):
    if list: 
        if list[0] == target: #checks if first element is target 
            return True
        else:
            return linSearch(list[1:],target) #recursive function moves through list until target is found
    return False

class linSearchTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(linSearch([3,5,7,1,2,9], 1))
    def testTwo(self):
        self.assertTrue(linSearch([3,5,7,1,2,9], 3))
    def testThree(self):
        self.assertTrue(linSearch([3,5,7,1,2,9], 5))
    def testFour(self):
        self.assertTrue(linSearch([3,5,7,1,2,9], 9))
    def testFive(self):
        self.assertTrue(linSearch([3,5,7,1,2,9], 7))
    def testSix(self):
        self.assertTrue(linSearch([3,5,7,1,2,9], 2))
    def testSeven(self):
        self.assertFalse(linSearch([3,5,7,1,2,9], 4))

def main():
    unittest.main()

if __name__ == '__main__':
    main()

import unittest

def palindrome(n):
    a = list(n) #converts input into list 
    reverse = a[::-1] #reverses list
    if a == reverse: #checks if input is equivalent to its reverse
        return True
    else:
        return False

class palindromeTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(palindrome([1,2,2,1]))

    def testTwo(self):
        self.assertFalse(palindrome([1,2,3,1]))

def main():
    unittest.main()

if __name__ == '__main__':
    main()


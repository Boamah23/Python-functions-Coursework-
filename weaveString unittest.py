import unittest

def weaveString(n,r):
    if not (n and r) : #checks if it doesnt exist 
        return n+r
    return(n[0] + r[0] + weaveString(n[1:], r[1:])) #recursive function takes first element of string n and adds it to the first element of string r then the second and so forth

class weaveStringTests(unittest.TestCase):

    def testOne(self):
        s = (weaveString("computer","code"))
        self.assertEqual(s, "ccoomdpeuter")
    def testTwo(self):
        s = (weaveString("computer", "computer"))
        self.assertEqual(s, "ccoommppuutteerr")
    def testThree(self):
        s = (weaveString("",""))
        self.assertEqual(s, "")
    def testFour(self):
        s = (weaveString("", "computer"))
        self.assertEqual(s, "computer")
    def testFive(self):
        s = (weaveString("computer", ""))
        self.assertEqual(s, "computer")
    def testSix(self):
        s = (weaveString("code","computer"))
        self.assertEqual(s, "ccoodmeputer")
    def testSeven(self):
        s = (weaveString("code","computer"))
        self.assertNotEqual(s, "sdfghhjkj")
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()

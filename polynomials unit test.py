import unittest
def pmultiply(p1,p2):
    degree1 = len(p1)-1
    degree2 = len(p2)-1
    finDegree = degree1 + degree2
    res = [0]*(finDegree+1)
    p1 = p1[::-1]
    p2 = p2[::-1]
    for i in range (0, degree1+1):
        for j in range (0, degree2+1):
            res[i+j] = res[i+j]+p1[i]*p2[j]
    res = res[::-1]
    print("Degree: " + str(finDegree))
    return(res)

class pmutiplyTests(unittest.TestCase):

    def testOne(self):
        s = (pmultiply([3,1,9],[2,1,2,1]))
        self.assertEqual(s, [6,5,25,14,19,9])
    def testTwo(self):
        s = (pmultiply([2,1,2,1],[3,1,9]))
        self.assertNotEqual(s, [1,5,21,3])
    def testThree(self):
        s = (pmultiply([2,1,2,1,2,1],[3,1,9,5,6,7]))
        self.assertNotEqual(s, [1,5,21,3])

def main():
    unittest.main()
if __name__ == '__main__':
    main()



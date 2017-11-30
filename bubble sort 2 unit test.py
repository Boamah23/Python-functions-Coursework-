import unittest
def bubbleSort(seq):
    for index in range(0,len(seq)-1): #outer loop has a range from n to n-1
        for j in range(0,len(seq)-1-index): #inner loop has a range from n to n-2(n-1-index)
            if seq[j] > seq[j+1]: #creates the condition where python can compare a value with the value to the right of it
                seq[j],seq[j+1]=seq[j+1],seq[j] #if the value to the right is bigger than the value to the left it will swap the two
                print(seq) # shows the new configuration of the sequence at each step
    return(seq) #returns all values in the for loop

class bubbleSortTest(unittest.TestCase):

    def testOne(self):
        s = (bubbleSort([2,7,9,4,1,5,3,6,0,8]))
        self.assertEqual(s, [0,1,2,3,4,5,6,7,8,9])
    def testTwo(self):
        s = (bubbleSort([2,7,9,4,1,5,3,6,0,8]))
        self.assertNotEqual(s, [2,7,9,4,1,5,3,6,0,8])
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()
    

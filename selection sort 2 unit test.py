import unittest
def selectionSort(list):
    for i in range(0,len(list)): #loop the number of elements times
        min = i #minimum number in list equals its position 
        for j in range(i,len(list)):
            if list[j] < list[min]: #checks for new min
                min = j #new min is assigned
        list[i], list[min] = list[min], list[i] #swap minimum with the current so the min will always go to front of list
    return(list)

class selectionSortTest(unittest.TestCase):

    def testOne(self):
        s = (selectionSort([2, 7, 9, 4, 1, 5, 3, 6, 0, 8]))
        self.assertEqual(s, [0,1,2,3,4,5,6,7,8,9])
    def testTwo(self):
        s = (selectionSort([2, 7, 9, 4, 1, 5, 3, 6, 0, 8]))
        self.assertNotEqual(s, [2, 7, 9, 4, 1, 5, 3, 6, 0, 8])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
        

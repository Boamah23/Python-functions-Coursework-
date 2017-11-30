import unittest
def insertionSort(seq):
  for index in range( 1,len(seq)):
    element = seq[index] #the current value equals its position in the sequence
    j = index #index equals the position
    while j > 0 and element < seq[j - 1]: #while position is bigger than 0 and current value is smaller than the value in the position before it
        seq[j] = seq[j - 1] #swap
        j = j - 1 #iterates
    seq[j] = element #position in sequence is equal to current value
  return seq

class insertionSortTests(unittest.TestCase):

  def testOne(self):
    s = (insertionSort([2, 7, 9, 4, 1, 5, 3, 6, 0, 8]))
    self.assertEqual(s, [0,1,2,3,4,5,6,7,8,9])
  def testTwo(self):
    s = (insertionSort([2, 7, 9, 4, 1, 5, 3, 6, 0, 8]))
    self.assertNotEqual(s, [[2, 7, 9, 4, 1, 5, 3, 6, 0, 8]])

def main():
  unittest.main()

if __name__ == '__main__':
  main()

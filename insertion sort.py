seq = [8,5,3,1,9,6,0,7,4,2,5]
def insertionsort(seq):
  for index in range( 1,len(seq)):
    element = seq[index]
    j = index
    while j > 0 and element < seq[j - 1]:
        seq[j] = seq[j - 1]
        j = j - 1
    seq[j] = element
  return seq
print(insertionsort(seq))

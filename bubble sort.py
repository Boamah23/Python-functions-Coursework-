#outer loop has a range from n to n-1
#inner loop has a range from n to n-2(n-1-index)
seq = [4,23,6,8,9,2]
def bubbleSort(seq):
    for index in range(0,len(seq)-1):
        for j in range(0,len(seq)-1-index):
            if seq[j] > seq[j+1]:
                seq[j],seq[j+1]=seq[j+1],seq[j]
    return(seq)
print(bubbleSort(seq))

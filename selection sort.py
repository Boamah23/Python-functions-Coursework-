def selectionSort(list):
    for i in range(0,len(list)):
        min = i
        for j in range(i,len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list
print(selectionSort([2,1,6,5,4,3]))

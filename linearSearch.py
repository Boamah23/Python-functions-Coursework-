target = int(input("Enter an integer "))

def linearSearch(array, target):
    if array:
        if array[0] == target:
            return str(target) + " has been found"
        else:
            return linearSearch(array[1:],target)

    return str(target) + " has not been found"

print(linearSearch([4,6,67,9,49],target))
print("Big O notation: O(N)")

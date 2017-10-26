n = input(str("enter a string: "))
def readReverse(n):
    if n == "":
        return n
    else:
        return readReverse(n[::-1])
print(readReverse(n))


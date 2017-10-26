from timeit import default_timer
n = input("Input a string: ")
r = 0
def readReverse(n):
    start = default_timer()
    r = len(n.split())
    if len(n) == 0:
        return n
    else:
        return n[0] + readReverse(n[::-1])
        duration = default_timer() - start
        print(str(r) + " words with a runtime of " + str(duration))
print(readReverse(n))

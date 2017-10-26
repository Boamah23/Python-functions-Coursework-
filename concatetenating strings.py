n = input(str("Enter a word: "))
r = input(str("Enter a second word: "))

def weaveString(n,r):
    n1 = list(n)
    r1 = list(r)
    if(len(n1)==len(r1)):
        print(''.join([str(a)+b for a,b in zip(n1,r1)]))
weaveString(n,r)

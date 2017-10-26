import time
n = int(input("Enter a number: "))
if n >= 231: 
    print("That value is too big, please enter a value below 231")
    time.sleep(3)
    n = int(input("Enter a number: "))
else:
    def factorial(n):
        fac = 1
        n1 = n
        while n1 >= 1:
            fac = fac * n1
            n1 = n1 - 1
        print(str(n)+"! = "+str(fac))
        time.sleep(2)
        r = int(input("Enter a number you wish to divide " + str(n)+"! by: "))
        t = fac % r
        if t == 0:
            print(str(r) + " divides " + str(n) + "!")
        else:
            print(str(r) + " does not divides " + str(n) + "!")
    
factorial(n)




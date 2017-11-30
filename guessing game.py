def guessingGame():
    bottom = 1
    top = 2000
    while True:
        mid = (bottom + top)//2 #finds midpoint
        x = input(str("Is this your number?: " + str(mid) + " "))
        if x == 'yes':
            print("Love thattt")
            break
        elif x == 'no':
            y = input(str("Is your number lower or higher: "))
            if y == 'lower':
                top = mid #top becomes midpoint if number is lower
            elif y == 'higher':
                bottom = mid #bottom becomes midpoint if number is higher
            else:
                break

guessingGame()
            

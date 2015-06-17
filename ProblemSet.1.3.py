
#takes FOREVER if epislon is set too low or if time given is too high

def payGuess(Bal, interest, time_given):
    epsilon = 700
    low = Bal/time_given
    high = ((Bal*interest)+Bal)/time_given
    guess = (high + low)/2
    newBal = Bal
    month = 1

    # make a loop to adjust guess
    while abs(newBal) > epsilon:

        # reset Balance to original
        newBal = Bal

        # make a loop with compounding interest to test guess 
        while month <= time_given:
            newBal = (newBal * (interest/12 + 1))
            newBal = newBal - guess
            month += 1

        # adjust payment or accept as answer
        if newBal<epsilon:
            high = guess
            guess = (high + low)/2
            month = 1
            
            
        else:
            low = guess
            guess = (high + low)/2
            month = 1
        
         
    print "Ending balance: $" + str(round(newBal, 2))
    print "Monthly payment needed: $" + str(round(guess, 2))
    print "Total paid: $" + str((round(guess, 2)) * time_given)

payGuess(17000, 0.07, 36)



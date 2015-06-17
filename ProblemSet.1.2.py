




def pay_it_off(Bal, payment, interest):
    nextBal = Bal
    while (nextBal > 0):
        month = 1
        payment += 10
        nextBal = Bal
        while (month <= (12*30) and nextBal > 0):
            intAddedBal = (nextBal * (interest/12 + 1))
            nextBal = intAddedBal - payment
            if nextBal<=0: continue
            month += 1
    else:
        print "Ending balance: $" + str(round(nextBal, 2))
        print "Monthly payment needed: $" + str(payment)
        print "Months needed: " + str(month) + " (Years: " + str(month/12) + ")"
    
        

pay_it_off(17000, 0, 0.07)

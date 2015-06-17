rebal = float(4800)
min_pay_rate = float(0.02)
annual_rate = float(0.2)

##rebal = float(raw_input("What is the current balance on your credit card?: "))
##annual_rate = float(raw_input("What is the annual interest rate?: "))
##min_pay_rate = float(raw_input("What is the minimum monthly payment rate?: "))



## Calculate Monthly Payment, Principal, Balance and Final Results
## Print outcome monthly and final 

def finalBal(rebal):
    month = 1
    totalPrin = 0
    totalPaid = 0
    while(month<=12):
        amountDue = rebal * min_pay_rate
        amountInterest = annual_rate / 12 * rebal
        amountPrin = amountDue - amountInterest
        totalPrin = totalPrin + amountPrin
        totalPaid = totalPaid + amountDue
        rebal = rebal - amountPrin
        print "______________________"
        print " "
        print "Month " + str(month)
        print " "
        print "Minimum payment due:" + str(round(amountDue, 2))
        print "Princibal paid: " + str(round(amountPrin, 2))
        print "Remaining balance: " + str(round(rebal, 2))
        month += 1
    print " "
    print "_____________________"
    print " "
    print "Results"
    print " "
    print "Total amount paid: " + str(round(totalPaid, 2))
    print "Final Balance: " + str(round(rebal, 2))    
    return 



finalBal(rebal)

print "Original balance: " + str(rebal)

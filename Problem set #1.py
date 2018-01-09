def Pay_minimum():
##Defining all the varialbes to perform calculations
    Bal = float(raw_input("Outstanding balance: "))
    Air = float(raw_input("Interest rate: "))
    Min_mon = float(raw_input("Minimum monthly payment rate: "))
    x = int(raw_input("How many months of payments would you like to proceed with?: "))
##Should end up with the Minimum monthly payment, priciple paid amount and remaining balance.
    for i in range(1,x):
        

        Min_mon_pay = Min_mon * Bal
        Int_paid = Air / 12 * Bal
        Prince_paid = Min_mon_pay - Int_paid
        Rem_bal = Bal - Prince_paid
        Bal = Rem_bal
        print 'Month: ', i
        print 'Minimum monthly payment: $', Min_mon_pay
        print 'Principle paid: $', Prince_paid
        print 'Remaining Balance: $', "%.2f" % Bal

##Will take raw input of outstanding balance and annual interest rate and output monthly payment to pay off debt
##in one year and number of months needed to pay debt. 
def Debt_off():
    Bal_input = float(raw_input("Outstanding balance: "))
    Bal = Bal_input
    Air = float(raw_input("Annual interest rate: "))    
    Mir = float(Air / 12.0)
    ans = 0
    months = 0

    while(Bal > 0):
        ans += 10
        Bal = Bal_input
        for i in range (1,13):
            Bal = (Bal * (1+Mir))- ans
            if (Bal <= 0):
                break
    print "Balance:", "%.2f" % Bal
    print ans
    print i


        

def Large_debt():
    Bal_input = float(raw_input("Outstanding balance: "))
    Bal = Bal_input
    Air = float(raw_input("Annual interest rate: "))    
    Mir = float(Air / 12.0)
    low = Bal / 12
    high = (Bal * ((1 + Mir)**12.0)/12.0)

    while(abs(Bal) >= 0.1):
        ans = ((low + high)/2)
        Bal = Bal_input
        for i in range (1, 13):
            Bal = Bal * (1 + Mir) - ans
        if (Bal < 0):
            high = ans
            print high
        else:
            low = ans
            print low
    print "Monthly payment to pay off debt in 1 year: ", "%.3f" % ans
    print "Number of months needed: ", i
    print "Balance: ", "%.2f" % Bal

##test harness

            
    
        
    
        
    
        

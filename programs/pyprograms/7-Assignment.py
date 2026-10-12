"""
Electricity bill calculator

Write a function to calculate electricity bill
use : unitsofelec consumption as the input to
the function

Logic:

unitsconsumed < 100 then cost/unit = 1 rupees
unitsconsumed>=100 <200 then cost/unit = 2 rupees
unitsconsumed>=200 <300 then cost/unit = 3 rupees
otherwise
cost/unit = 5 rupees

"""
def elecbillgen(unitsconsumed):
    billamount=0
    rate=0
    if(unitsconsumed<100):
        rate=1
    elif(unitsconsumed>=100 and unitsconsumed<200):
        rate=2
    elif(unitsconsumed>=200 and unitsconsumed<300):
        rate=3
    else:
        rate=5
    billamount=unitsconsumed*rate
    print("Your bill amount is ",billamount)

units=int(input("Enter units consumed"))
elecbillgen(units)
    



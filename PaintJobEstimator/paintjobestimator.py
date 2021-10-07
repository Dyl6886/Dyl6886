import math
while (True):
    while (True):
        try:
            WallSpace = float(input("Please enter the amount of wall space to be painted in square feet. "))
            while WallSpace < 1:
                WallSpace = input("Please enter a positve amount for the area of wall to be painted. ")
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    while (True):
        try:
            ppg = float(input("Please enter the price per gallon of paint. "))
            while ppg < 1:
                ppg = input("Please enter a positive amount for the price of paint per gallon. ")
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break
    
    cph = 62.25
    #cost per hour
    ttp = 6*(WallSpace/350)
    TotalTime = round(ttp, 1)
    #time to paint
    paint = WallSpace/350
    TotalPaint = int(math.ceil(paint))
    #amount of paint
    PaintCost = ppg * TotalPaint
    #cost of paint
    labor = cph * ttp
    #cost of labor
    cost = labor + PaintCost
    #final cost
    

    print("Gallons of Paint: "+str(TotalPaint))
    print("Hours of Labor: "+str(TotalTime))
    print("Cost of Paint: $"+"{:.2f}".format(PaintCost))
    print("Cost of Labor: $"+"{:.2f}".format(labor))
    print("Total Cost: $"+"{:.2f}".format(cost))
    again = input("Would you like to do another estimate? (y/n) ")
    if again != 'y':
        break

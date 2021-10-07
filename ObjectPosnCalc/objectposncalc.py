go = "y"
while go == "y":
    while (True): 
        try:
            ip = float(input("What is the initial position of the object in meters?  "))
        except ValueError:
	        print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break
    
    while (True): 
        try:
                iv = float(input("What is the initial velocity of the object in meters per second? "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    while (True): 
        try:
            a = float(input("What is the acceleration of the object in meters per second squared? "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    while (True):
        try:
            t = float(input("What is the amount of time passed in seconds? "))
            while t < 0:
                t = float(input("Please type in a positive amount for the time passed in seconds."))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid. ")
        else:
            break

    #xf = x0 + v0t + ½at2

    c = iv * t
    b = .5 * a * (t**2)

    xf = ip + c + b

    print(xf)
    again = input("If you would like to perform another calculation, type y. ")
    if again == "y":
        go = "y"
    else:
        go = "n"
    

import random
file = open('randomnum.txt','w')

while (True):
    try:
        NumOfNum = int(input("How many numbers do you want? "))
        while int(NumOfNum) < 1:
            NumOfNum = input("Please enter a positive integer ")
    except ValueError:
        print("The value you enetered is invalid. Only integers are valid. ")
    else:
        break
    
while (True):
    try:
        Min = int(input("What is the lowest the random number should be? "))
        while int(Min) < 1:
            Min = input("Please enter a positive integer ")
    except ValueError:
        print("The value you enetered is invalid. Only integers are valid. ")
    else:
        break
    
while (True):
    try:
        Max = int(input("What is the highest the random number should be? "))
        while int(Max) < 1:
            Max = input("Please enter a positive integer ")
    except ValueError:
        print("The value you enetered is invalid. Only integers are valid. ")
    else:
        break

#print(NumOfNum)
#print(Max)
#print(Min)


for x in range(NumOfNum):
    temp = random.randrange(int(Min),int(Max))
    #print(temp)
    file.write(str(temp) +' \n' )
file.close()
print("The random numbers were written to randomnum.txt")

import math
import os
from statistics import multimode
while (True):
    while (True):
        try:
            fp = input("What is the file name? ")
            file = open(fp)
        except OSError:
            print("The filename entered does not exist. ")
        else:
            break


#    if (any(char.isdigit() for char in file) == True):
#        print("No numbers were found in the file")
#        cont = "f"
#    else:
#        cont = "t"


    list = [int(num) for num in file.read().split()]
    list.sort()
    #for num in list:
    #    print(num)

    count = len(list)
    Sum = sum(list)
    Max = max(list)
    Min = min(list)
    avg = Sum / count
    Range = Max - Min

    evenodd = "n/a"

    if (count % 2 == 0):
        evenodd = "Even"
    elif (count % 2 == 1):
        evenodd = "Odd"

    if (evenodd == "Odd"):
        Median = list[len(list) // 2]
    elif (evenodd == "Even"):
        m1 = list[count //2]
        m2 = list[count //2 - 1]
        Median = (m1 + m2)/2

    Mode = multimode(list)

    print("File name: " + str(fp))
    print("Sum: " + str(Sum))
    print("Count: " + str(count))
    print("Average: " + str(avg))
    print("Maximum: " + str(Max))
    print("Minimum: " + str(Min))
    print("Range: " + str(Range))
    print("Median: " + str(Median))
    print("Mode " + str(Mode))

    file.close()
    end = input("Would you like to evaluate another file? (y/n)" )
    if (end != "y"):
        break

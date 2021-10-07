import math
while (True):
    try:
        fp = input("What is the file name? ")
        file = open(fp)
    except OSError:
        print("The filename entered does not exist. ")
    else:
        break

list = [int(num) for num in file.read().split()]

count = len(list)
Sum = sum(list)
Max = max(list)
Min = min(list)
avg = Sum / count
Range = Max - Min


print("File name: " + str(fp))
print("Sum: " + str(Sum))
print("Count: " + str(count))
print("Average: " + str(avg))
print("Maximum: " + str(Max))
print("Minimum: " + str(Min))
print("Range: " + str(Range))

file.close()

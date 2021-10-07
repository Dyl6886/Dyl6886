file = open('randomnum.txt', 'r')
#print(count)

print("List of numbers in randomnum.txt: ")
line = file.readline()
count = 1
while line:
    print(line.strip())
    line = file.readline()
    count += 1
print("Random Number Count: " + str(count-1))
file.close()

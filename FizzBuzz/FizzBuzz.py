number = 1

while number < 101:
    three = number % 3
    five = number % 5
    if three == 0 and five != 0:
        print("fizz")
    elif five == 0 and three != 0:
        print("buzz")
    elif five != 0 and three != 0:
        print(number)
    else:
        print("fizzbuzz")
    number = number + 1

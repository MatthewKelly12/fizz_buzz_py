for num in range(1, 31):
    if (num % 15 == 0):
        print(num, "fizzBuzz")
    elif (num % 5 == 0):
        print(num, "Buzz")
    elif (num % 3 == 0):
        print(num, "fizz")
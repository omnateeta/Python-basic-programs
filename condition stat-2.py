# condition is checked by the outer if statement?
number = int(input())

if number > 0:
    print("The number is positive")
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

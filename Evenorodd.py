#Program to accept a number from the user and determine whether it is even or odd

Number = int(input("Enter the number : "))
if Number == 0:
    print(f"The Entered Number {Number} is even")
elif (Number%2) == 0:
    print(f"The Entered Number {Number} is even")
else:
    print(f"The Entered Number {Number} is odd")

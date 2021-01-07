#Program to accept two numbers from the user and determine bigger of the two

Number1 = int(input("Enter the First number : "))
Number2 = int(input("Enter the Second number : "))

if Number1 > Number2:
    print(f"The bigger of the two numbers entered ({Number1} and {Number2}) is: {Number1}")
else:
    print(f"The bigger of the two numbers entered ({Number1} and {Number2}) is: {Number2}")
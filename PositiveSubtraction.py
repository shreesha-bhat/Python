#Program to accept two numbers num1 and num2; when one is subtracted from the other, 
# the result should always be a positive number

Number1 = int(input("Enter the First number : "))
Number2 = int(input("Enter the Second number : "))

Sub = Number1 - Number2

if Sub < 0:
    print("The result (difference) is : ",(Sub*-1))
else:
    print(f"The result (difference) is : {Sub}")
#Program to find biggest of three

Num1 = int(input("Enter the First number : "))
Num2 = int(input("Enter the Second number : "))
Num3 = int(input("Enter the third number : "))

if (Num1 > Num2) and (Num1 > Num3):
    print("The biggest of the 3 numbers entered is : ",Num1)
elif (Num2 > Num1) and (Num2 > Num3):
    print("The biggest of the 3 numbers entered is : ",Num2)
else:
    print("The biggest of the 3 numbers entered is : ",Num3)
    
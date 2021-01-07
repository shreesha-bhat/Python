#Pprogram to convert a number to positive if its negative

Number = int(input("Enter the number : "))

if Number < 0:
    print("The result is : ",(Number*-1))
else:
    print("The result is : ",Number)
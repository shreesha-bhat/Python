#Program to calculate Simpleintrest

Pamount = int(input("Enter the principal amount : "))
Intrest = float(input("Enter the rate of interest : "))
Time = int(input("Enter the time (years) : "))

print("Simple Intrest : ",int(((Pamount*Time*Intrest)/100)))
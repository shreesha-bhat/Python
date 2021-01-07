#Program to swap numbers

Number1 = int(input("Enter the First number : "))
Number2 = int(input("Enter the Second number : "))
print(f"Before swap, the values of num1 = {Number1} and num2 = {Number2}")

Number1 = Number1 + Number2
Number2 = Number1 - Number2  
Number1 = Number1 - Number2   

print(f"After swap, the values of num1 = {Number1} and num2 = {Number2}")
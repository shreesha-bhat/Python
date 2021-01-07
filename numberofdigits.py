#program to find number of dights in a number

num = int(input("Enter any number : "))
digits = 0
while num >= 10:
    num /=  10
    digits += 1

print("The number of digits in the entered number is ",digits+1)
    
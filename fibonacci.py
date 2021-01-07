#program to find fibonacci series

num = int(input("Enter the upper bound number to generate the Fibonacci numbers : "))
num1 = 0
num2 = 1
series = 0
print("Fibonacci series up to the entered number is : ",end=' ')
for i in range(num):
    if series > num:
        break
    print(series, end=' ')
    num1 = num2
    num2 = series
    series = num1 + num2
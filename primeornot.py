#Program to find a number is prime or not
num = int(input("Enter a number: "))

if num > 0:
    for i in range(2,num):
        if (num % i) == 0:
           print(f"The entered number {num} is not a prime number.")
           break
    else:
        print(f"The entered number {num} is a prime number.")

else:
   print(f"The entered number {num} is less than 0.")
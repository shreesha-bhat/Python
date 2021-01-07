#Program to generate the first 'N' natural numbers. Accept the value of 'N' from the user

N = int(input("Enter Value of N : "))
print(f"First {N} natural numbers are : ")

for i in range(N):
   print(i+1, end=' ')

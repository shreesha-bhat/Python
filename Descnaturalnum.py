#Program to print natutal numbers in descending order

N = int(input("Enter the number of natural numbers to be generated : "))
print(f"The first {N} natural numbers in descending order are :", end=' ')

for i in range(N):
   print(N-i, end=' ')
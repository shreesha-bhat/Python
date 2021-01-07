#Program to accept a number “n” from the user; then display the series 1,3,5,7,9,…,n 
# and find the sum of the numbers in this series

num = int(input("Enter the value of n : "))
aN = 1
print("The series is : ",end=' ')
for i in range(1,num+1):
    if i != num:
        print(aN,end=',')
    if i == num:
        print(aN)
        last = aN
    aN = aN + 2

print("Sum of the Series : ",int(((num*(1 + last) / 2))))
    
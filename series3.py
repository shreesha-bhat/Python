#Program to accept a number “n” from the user; find the sum of the series 1/23+1/33+1/43……..+1/n3

num = int(input("Enter the value of N : "))
sum = 0
for i in range(1,num+1):
    if i == 1:
        print(i,end='+')
    if i != 1 and i != num:
        print(f"1/{i}^3",end='+')
    if i == num:
        print(f"1/{i}^3")
    sum += 1/(i * i * i)

print("Sum of the series is : ",round(sum,2))


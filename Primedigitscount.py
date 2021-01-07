num = int(input("Enter any number : "))
count = 0
while num > 0:
    flag = 0
    rem = int(num % 10)
    num = num // 10
    for i in range(2,rem):
        if (rem % i) == 0:
            flag = 1
            break
    if flag == 0:
        count += 1
print("Total Prime numbers : ",count)
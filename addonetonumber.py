
num = int(input("Enter any number : "))
sum = 0
temp_sum = 0
while(num != 0):
    r = num % 10
    temp = r + 1
    if temp == 10:
        temp = 0 
    num = num // 10
    sum = (sum * 10) + temp
    
while(sum!=0):
    i = sum % 10
    sum = sum // 10
    temp_sum = (temp_sum * 10) + i
    
print("The number after adding 1 to each digit : ",temp_sum)
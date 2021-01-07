#Program to display prime numbers from user input

lower = int(input("Enter the lower bound value : "))
upper = int(input("Enter the upper bound value : ")) 
print(f"The prime numbers between {lower} and {upper} are:", end=' ')
for i in range(lower,upper+1):
    flag = 0
    for j in range(2,i):
        if ((i % j) == 0) and (j >= 2):
            flag = 1
    if flag == 0:
        print(i, end=' ')
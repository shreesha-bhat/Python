#Program to accept a number “n” from the user; then display the sum of the series 1+1/2+1/3+……….+1/n

num = int(input("Enter the value of N : "))

for i in range(1,num+1):
    if i == 1:
        print(i,end='+')
    if i != 1 and i != num:
        print(f"1/{i}",end='+')
    if i == num:
        print(f"1/{i}",end='')
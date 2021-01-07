#Program to Draw the pattern as shown in 27th question


for i in range(1,6):
    num = 0
    for j in range(1,6):
        if j > i:
            print("",end=' ')
        else:
            num += 1
            print(num,end=' ')
    print("")
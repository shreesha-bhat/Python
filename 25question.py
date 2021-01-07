#Program to Draw the pattern as shown in 25th question

num = 0
for i in range(1,5):
    for j in range(1,5):
        if j > i:
            print("",end=' ')
        else:
            num += 1
            print(num,end=' ')
    print("")
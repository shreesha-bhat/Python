#Program to Draw the pattern as shown in 30th question

odd = 1
for i in range(1, 6):   
    num = 0 
    for j in range(1, 10): 
        if j > odd:
            print("",end=' ')
        else:
            if j > i:
                num -= 1
                print(num,end=' ')
            else:
                num += 1
                print(num,end=' ')
    odd += 2
    print(" ")  
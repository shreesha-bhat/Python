#Program to Draw the pattern as shown in 33th question

even = 2
for i in range(1, 5):   
    num = 0 
    for j in range(1, 10): 
        if j > even:
            print("",end=' ')
        else:
            if j > i:
                print(num,end=' ')
            else:
                num += 1
                print(num,end=' ')
    even += 2
    print(" ")  
#Program to Draw the pattern as shown in 28th question


for i in range(6, 0, -1):   
    num = 0 
    for j in range(0, i - 1): 
        num += 1 
        print(num, end=' ')  
    print(" ")  
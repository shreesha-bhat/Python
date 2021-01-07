#Program to Draw the pattern as shown in 35th question

for i in range(1,8):
    for j in range(1,11):
            if i == 1 or i == 7:
                print("*",end='')
            if (j == 5) and ( i != 1 and i != 7):
                print("*",end='')
            if (j != 5) and ( i != 1 and i != 7):
                print("",end=' ')
    print("")
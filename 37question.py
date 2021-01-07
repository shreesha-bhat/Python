#Program to Draw the pattern as shown in 37th question

for i in range(1,8):
    for j in range(1,13):
            if i == 4:
                print("*",end='')
            if i == 1 and j < 7:
                print("*",end='')
            if i == 1 and j > 7:
                print(" ",end='')
            if i == 7 and j >= 7:
                print("*",end='')
            if i == 7 and j < 7:
                print(" ",end='')
            if j == 7 and (i != 1 or i != 7 or i != 4):
                print("*",end='') 
            if j != 7 and (i != 1 or i != 7 or i != 4):
                 print("",end='')
    print("") 
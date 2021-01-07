#Program to Draw the pattern as shown in 36th question

for i in range(1,6):
    for j in range(1,5):
            if i == 1 or i == 3:
                print("@ ",end=' ')
            if (j == 1 or j == 4) and ( i != 1 and i != 3):
                print("@ ",end=' ')
            if (j != 1 or j != 4) and ( i != 1 and i != 3):
                print(" ",end=' ')
    print("")   
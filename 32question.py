#Program to Draw the pattern as shown in 32th question

val = 65
for i in range(1,4):
    for j in range(1,4):
            ch = chr(val)
            print(ch,end=' ')
            val += 1
    print("")
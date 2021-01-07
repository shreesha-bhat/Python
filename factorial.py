num = int(input("Enter any number : "))
factorial = 1
if num < 0:
   print("Enter positive number")
elif(num == 0):
    print("The factorial of 0 is 1")
else:
  while(num>0):
        factorial = factorial*num
        num = num - 1
        
  print("factorial of the entered number is : ",factorial)
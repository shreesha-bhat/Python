#program to accept a number from the user and find the reverse of the entered number

number = int(input("Enter any number : "))  
rev = 0    
  
while (number > 0):
    remainder = number % 10  
    rev = (rev * 10) + remainder  
    number //= 10   
print("Reverse of the entered number is ",rev)  
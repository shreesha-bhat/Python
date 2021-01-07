# program to accept a number from the user and find the sum of digits in the entered number

Number = int(input("Enter any Number : "))
Sum = 0

while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10

print("The sum of digits of the entered number is",Sum)
#Program to give Members 10% discount and others 3%

Bill = int(input("Enter Bill Amount : "))
Card = str(input("Do you have a membership Card : "))
Uppercard = Card.upper()

if Uppercard == 'Y':
    print(f"Thank you! Your total bill amount is Rs {Bill}, discount is Rs {int(Bill*(10/100))} and net amount payable is Rs {int(Bill-(Bill*(10/100)))}.")
else:
    print(f"Thank you! Your total bill amount is Rs {Bill}, discount is Rs {int(Bill*(3/100))} and net amount payable is Rs {int(Bill-(Bill*(3/100)))}.")
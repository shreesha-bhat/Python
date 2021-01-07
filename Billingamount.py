#Program to accept the billing amount, if it is > 6000 then give a discount of 10%

Amount = int(input("Enter the Billing Amount : "))

if Amount > 6000:
    print("Your net billing amount : ", int((Amount-(Amount*(10/100)))))
else:
    print("Your net billing amount : ", (Amount))
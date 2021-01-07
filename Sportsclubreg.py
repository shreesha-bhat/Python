#Program to Display messages depending upon the age(18 or greater)

Name = str(input("Enter the Name : "))
Mobile = int(input("Enter the mobile Number : "))
Age = int(input("Enter the age : "))

if Age < 18:
    print("Sorry! You need to be at least 18 years old to get membership.")
else:
    print(f"Congratulations {Name} for your successful registration.")
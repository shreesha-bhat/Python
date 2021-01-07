#Program to calculate employee salary per year

EmpID = int(input("Enter emp ID : "))
Name = str(input("Enter Employee name : "))
Salary = int(input("Enter Monthly Salary : "))
Yearly = Salary*12

print(f"Hi {Name} Your employee id is {EmpID}, monthly salary is Rs "+"{:,}".format(Salary) +" and yearly salary is Rs "+"{:,}".format(Yearly))
#Program to calculate Average weight

Weight1 = float(input("Enter the weight of the first person : "))
Weight2 = float(input("Enter the weight of the second person : "))
Weight3 = float(input("Enter the weight of the third person : "))

Sum = round((Weight1 + Weight2 + Weight3),1)
Avg = round(((Weight1+Weight2+Weight3)/3),1)

print(f"The sum of weight of the 3 persons is {Sum} and the average weight is {Avg}")
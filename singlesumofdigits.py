#program to accept a number from the user and calculate the sum of digits of the number

def sumofdigits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10

    if sum > 9:
        return sumofdigits(sum)

    return sum

n = int(input("Enter any number : "))
print("Single digit sum is :",sumofdigits(n))


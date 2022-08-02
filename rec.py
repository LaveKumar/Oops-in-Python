# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
"""def factorial(n):

        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1

    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number = int(input("Enter the number  "))
print(factorial(number))"""
# Using recurison
def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)
number=int(input("Enter the number\n"))
print(factorial(number))


print("Enter the numbers")
num1 = input()
num2 = input()
try:
    print("The sum of these numbers",
          int(num1)+int(num2))
except Exception as e:
    print(e)


print("Something is very very important")
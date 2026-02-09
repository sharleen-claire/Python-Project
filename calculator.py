num1 = float(input("Enter a number: "))
operators =input("Enter operators(+, -,*,/): ")
num2 = float(input("Enter second number: "))

if operators == "+":
    print(num1 + num2)
elif operators == "-":
    print(num1 - num2)
elif operators == "*":
    print(num1 * num2)
elif operators == "/":
    print(num1 / num2)
else:
    print("Invalid operator")



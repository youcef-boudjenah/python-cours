import calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
calculator.add(num1, num2)
calculator.subtract(num1, num2)

print("Addition of", num1, "and", num2, "is:", calculator.add(num1, num2))
print("Subtraction of", num1, "and", num2, "is:", calculator.subtract(num1, num2))
print("Program executed successfully.")


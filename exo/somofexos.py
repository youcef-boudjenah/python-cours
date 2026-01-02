# Ask the user for a number and print its multiplication table (1 to 10). in python

number = int(input("Enter a number: "))
print(f"Multiplication table of {number}:")

for i in range(1, 11):
   print(f"{number} x {i} = {number * i}")
   print( "number  * " , i , " =  " , number * i)









n = 5
for i in range(1, n + 1):
    print("A" * (n - i + 1) )


# i = 5 - 1 + 1 = 5
# i = 5 - 2 + 1 = 4
# i = 5 - 3 + 1 = 3
# i = 5 - 4 + 1 = 2
# i = 5 - 5 + 1 = 1









# Ask the user for a password.
# Rules:
# At least 8 characters
# Contains 1 number
# Contains 1 uppercase letter
# Print:
# Strong password
# or Weak password







password = input("Enter your password: ")
has_number = False
has_uppercase = False
for char in password:
    if char.isdigit():
        has_number = True
    if char.isupper():
        has_uppercase = True
        
if len(password) >= 8 and has_number and has_uppercase:
    print("Strong password")
else:
    print("Weak password")

























# *
# **
# ***
# ****
# *****

n = 5

for i in range(1, n + 1):
    print("*" * i)

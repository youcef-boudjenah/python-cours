
# # def greet():
# #     print("Hello, welcome to the Python functions course!")

# # greet()
# # greet()
# # greet()
# # greet()
# # greet()
# # greet()
# # greet()
# # greet()











# def add(a, b = 0):
#     return a + b

# result = add(5)
# print( result)














# def power(base, exponent=2 , test):
#     return base ** exponent

# print("3 squared is", power(3))
# print("3 cubed is", power(5, 3 ))










# # 6. Function with multiple return values
# def get_min_max(numbers):
#     return min(numbers), max(numbers)

# nums = [4, 7, 1, 9]
# minimum, maximum = get_min_max(nums)
# print("Min:", minimum, "Max:", maximum)


















# # 7. Keyword arguments
# def introduce(name, age):
#     print(f"My name is {name} and I am {age} years old.")

# introduce(name="Alice" , age=25 )







# # 8. Variable number of arguments
# def print_all(*args):
#     for arg in args:
#         print(arg)

# print_all("apple", "banana", "cherry", "cherry" ,"cherry")







# # 9. Lambda functions (anonymous functions)
# square = lambda x: x * 5
# print("Square of 6 is", square(6))











# # 10. Docstrings
# def multiply(a, b):
#     """Multiply two numbers and return the result."""
#     return a * b

# print(multiply.__doc__)
# print("2 * 4 =", multiply(2, 4))









# # Practice: Try writing your own functions!
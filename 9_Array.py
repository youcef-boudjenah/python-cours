# import array
# import numpy as np

# # 9_Array.py
# # Python Course: Arrays

# """
# Arrays are data structures that store multiple values in a single variable.
# In Python, the built-in array type is called 'list', but you can also use the 'array' module for more efficient storage of numeric data.
# """

# # 1. Lists as Arrays
# # Lists can store elements of any type.

# numbers = [1, 2, 3, 4, 5]
# print("List:", numbers)

# # Accessing elements
# print("First element:", numbers[0])
# print("Last element:", numbers[-1])

# # Slicing
# print("First three elements:", numbers[:3])

# # Modifying elements
# numbers[2] = 10
# print("Modified list:", numbers)

# # Adding elements
# numbers.append(6)
# print("After append:", numbers)

# numbers.insert(1, 7)
# print("After insert:", numbers)

# # Removing elements
# numbers.remove(7)
# print("After remove:", numbers)

# del numbers[0]
# print("After deleting first element:", numbers)

# # Length of array
# print("Length:", len(numbers))

# # Iterating over array
# for num in numbers:
#     print("Element:", num)

# # 2. Using the array module

# # Create an array of integers
# arr = array.array('i', [1, 2, 3, 4, 5])
# print("Array module:", arr)

# # Accessing and modifying
# arr[0] = 10
# print("Modified array:", arr)

# # Adding and removing
# arr.append(6)
# arr.pop()
# print("After append and pop:", arr)

# # 3. Multidimensional Arrays (Lists of Lists)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print("Matrix:", matrix)
# print("Element at row 2, col 3:", matrix[1][2])

# # Iterating over 2D array
# for row in matrix:
#     for item in row:
#         print(item, end=' ')
#     print()

# # 4. Useful List Methods
# numbers = [3, 1, 4, 1, 5, 9, 2]
# print("Original:", numbers)
# numbers.sort()
# print("Sorted:", numbers)
# numbers.reverse()
# print("Reversed:", numbers)
# print("Count of 1:", numbers.count(1))
# print("Index of 5:", numbers.index(5))

# # 5. List Comprehensions
# squares = [x**2 for x in range(10)]
# print("Squares:", squares)

# # 6. Numpy Arrays (for advanced usage)

# np_arr = np.array([1, 2, 3, 4, 5])
# print("Numpy array:", np_arr)
# print("Numpy array multiplied by 2:", np_arr * 2)

# # 7. Summary
# """
# - Lists are the most common array-like structure in Python.
# - The array module provides type-restricted arrays for numbers.
# - For large, efficient numeric arrays, use numpy.
# - Arrays can be single or multi-dimensional.
# - Lists have many useful methods for manipulation.
# """

# # End of course on arrays in Python.
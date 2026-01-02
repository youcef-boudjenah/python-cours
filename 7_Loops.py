# 7_Loops.py
# Introduction to Loops in Python

# 1. For Loop





for i in range(9000):
   print("The number is", i)







count = 0
while count < 9000:
    if count % 2  == 0 :
        print("The number is even", count)
    else :
        print("The number is odd", count)
    count += 1










# 3. Looping through a list
# print("\nLooping through a list:")
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)








for num in range(10):
    if num == 5:
        break 
    if num % 2 == 0:
        continue  
    print("Odd number:", num)




# print("\nCollecting odd numbers:")
# for numbers in range(10) : 
#     num = [] ;
#     if numbers % 2 != 0 : 
#         num.append(numbers)
#         print(num) ;





for i in range(3):
    for j in range(2):
        print( "i = " , i  , "j = " , j ) 
# num = " boudjenah youcef" 
# isexistee = "e" in num 
# print(isexistee)

# print("////////////")

# count  = 0
# for i in num :
#     if i == "e" :
#         count += 1
# print( "count of E is : " , count)

# print("////////////")


# new  = num.join("*")
# print(new)

# print("////////////")

# userinput = input("enter a character : ")
# inverse  = userinput[::-1]
# print("inverse is : " + inverse)

# print("////////////")

# if userinput == inverse :
#     print("palindrome")
# else :
#     print("not palindrome")

# les unsemble initiales

X = {'a', 'b' , 'c' , 'd'}
Y = {'s', 'b' , 'd' , 'a'}

# print(X)
# print(Y)
# print("////////////")
# print(X.union(Y))
# print("////////////")
# print(X.intersection(Y))
# print("////////////")

# print(X.difference(Y))
# print("////////////")
# print(Y.difference(X))

# print("////////////")

isAinY = 'a' in Y
print(isAinY)

# print("////////////")
# iscinX = 'c' in X
# print(iscinX)

def f(a,b) :
  if b==1 :
   return a
  return a+f(a,b-1)

print(f(3,5))
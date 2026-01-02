import random

secret = 2006
lamda = 0
 
print("Guess the password:")
state = True
while state:
    lamda += 1
    guess = int(input("Your guess: "))

    if guess < secret:
        print("Higher!")
        if lamda == 10 : 
            state = False
    elif guess > secret:
        print("Lower!")
    else:
        print("🎉 Correct! You guessed the number!")
        break


import random
print("Welcome! This is a guessing game where you provide an upper and lower bound," \
" and you must guess the number in just 10 tries!")

upper = int(input("\n\n Upper Bound: "))
lower = int(input("\n Lower Bound: "))

num = random.randint(lower, upper)

guessCount = 0
maxGuess = 10

while (guessCount < maxGuess):
    userGuess = int(input("Enter your guess: "))
    if (userGuess > num):
        print("Try Again! Your guess was too high!\n")
    elif (userGuess < num):
        print("Try Again! Your guess was too low!\n")
    elif (userGuess == num):
        print("Great Job! The number was: ", num)
        break
    if (guessCount == maxGuess - 1):
        print("Sorry! The number was: ", num)
        break
    guessCount = guessCount + 1
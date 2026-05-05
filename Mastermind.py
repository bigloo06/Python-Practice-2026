import random

num = str(random.randint(1000, 9999))

guess = input("Guess a 4 digit number: ")

if (guess == num):
    print('Wow! Only one try! You are a true mastermind!')
else:
    tries = 0
    while (guess != num):
        tries += 1
        correct = 0

        correctDigit = ['X'] * 4

        for i in range(4):
            if (guess[i] == num[i]):
                correct += 1
                correctDigit[i] = guess[i]
            else:
                continue

        if(correct == 0):
            print('None of the numbers match')
        else:
            print('You got ', correct, ' digits correct')
        guess = input('Enter your next guess: ')
    if guess == num:
        tries += 1
        print('You are a mastermind!')
        print('It took', tries, 'tries.')
    
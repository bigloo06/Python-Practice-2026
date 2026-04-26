import random
from collections import Counter

fruits = ['apple', 'orange', 'banana', 'apricot', 'lemon', 'lime', 'cherry',
          'tangerine', 'plum', 'peach', 'melon', 'pear', 'jackfruit']
fruit = random.choice(fruits)

if __name__ == '__main__':
    print("Welcome to fruit Hangman!")
    print("You must guess the fruit through letters!")

    guessed = ''
    turn = len(fruit) + 3
    flag = 0
    try:
        while turn > 0 and flag == 0:
            if turn > 1:
                print(turn, "chances left!")
            else:
                print(turn, "chance left!")
            turn -= 1

            for char in fruit:
                if char in guessed:
                    print(char)
                else:
                    print('_')

            try:
                guess = input('Enter a letter: ').lower()
            except:
                print('Enter only a valid letter.')
                continue
            if not guess.isalpha():
                print('Enter only a valid letter.')
                continue
            elif len(guess) > 1:
                print('Enter only a valid letter.')
                continue
            elif guess in guessed:
                print('This letter has already been guessed.')
                continue
            if guess in fruit:
                guessed += guess * fruit.count(guess)
            if Counter(guessed) == Counter(fruit):
                print("\nCongrats! The word was:", fruit)
                flag = 1
                break
        if turn <= 0 and Counter(guessed) != Counter(fruit):
            print('\nSorry, you lost! The word was:', fruit)
    except KeyboardInterrupt:
        print('Game interrupted.')
        exit()
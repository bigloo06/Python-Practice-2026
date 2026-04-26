import random
name = input("What is your name? ")
print(name, "you must guess the word through its characters! ")

words = ['hello', 'world', 'python', 'art', 'music', 'computer', 'science', 'program',
         'game', 'fun', 'creativity', 'player', 'hopeful']

word = random.choice(words)

guesses = ''
turns = 10

while(turns > 0):
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("Congrats", name, "you win!")
        print("The word was:", word)
        break
    guess = input("\nGuess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print('Wrong!')
        if turns == 0:
            print("You lose!")
            print("The word was:", word)
            break
        print('You have', turns, 'more guesses')
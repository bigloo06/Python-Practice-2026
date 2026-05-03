def nearestMultiple(last):
    if last >= 4:
        near = last + (4 - (last % 4))
    else:
        near = 4
    return near

def check(nums):
    i = 1
    while i < len(nums):
        if(nums[i] - nums[i-1]) != 1:
            return False
        i += 1
    return True

def lose():
    print("\nSorry you lose!")
    exit()

def startGame():
    nums = []
    last = 0
    while game:
        print('Enter either F (first) or S (second) to indicate if you want to go first or second')
        order = input('').upper()
        if order == 'F':
            while game:
                if last == 20:
                    lose()
                print('\nIt is your turn.')
                num = int(input('How many numbers are you entering? (1-3)\n'))
                if 1 <= num <= 3:
                    comp = 4 - num
                else:
                    print('Enter a number between 1 and 3')

                print('Enter your numbers:')
                for _ in range(num):
                    nums.append(int(input('')))

                last = nums[-1]

                if not check(nums):
                    print('Integer must be consecutive, you are disqualified!')
                    lose()
                if last == 21:
                    lose()
                
                print("\nIt is the Computer's turn.")
                for i in range(1, comp + 1):
                    nums.append(last + i)
                print("Numbers after the Computer's turn:", nums)
                last = nums[-1]
        elif order == 'S':
            comp = 1
            last = 0
            while last < 20:
                print("\nIt is the Computer's turn.")
                for i in range(1, comp + 1):
                    nums.append(last + i)
                print("Number's after the Computer's turn:", nums)
                if nums[-1] == 20:
                    lose()
                
                print('\nIt is your turn.')
                num = int(input('How many numbers are you entering? (1-3)\n'))
                if 1 <= num <= 3:
                    comp = 4 - num
                else:
                    print('Enter a number between 1 and 3')

                print('Enter your numbers:')
                for _ in range(num):
                    nums.append(int(input('')))
                last = nums[-1]

                if not check(nums):
                    print("\nYou didn't enter consecutive integers")
                    lose()
                near = nearestMultiple(last)
                comp = near - last
                if comp == 4:
                    comp = 3
            
            print('\n\nCongrats! You win!')
            exit()
        else:
            print('Enter either "F" or "S".')

if __name__ == '__main__':
    game = True
    while game:
        start = input('Are you ready to play?\n').lower()
        if start == 'yes':
            startGame()
        elif start == 'no':
            exit()
        else:
            print("Sorry, didn't get that, try entering yes or no")
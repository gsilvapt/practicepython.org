#!/usr/bin/env/python3
def guessingGame():
    """
    by: gsilvapt
    Function that generates a random integer from 1 to 9 and asks user
    to guess the number. It provides feedback (lower, higher) accordingly.
    Function keeps tracks of the bumber of attemps and uses that data
    (int) -> str
    """
    import random
    random_num = random.randint(1,10)
    attempts = 0
    flag = False        # To keep running until there's a match
    while flag != True:
        num = input('I generated a number. Want to guess it? ')
        if type(num) is int and int(num) == random_num:
            attempts += 1
            print('Great! You guessed it in ' + str(attempts) + ' attempts.')
            flag = True
        elif type(num) is int and int(num) < random_num:
            attempts += 1
            print ('Too low! Try higher: ')
        elif type(num) is int and int(num) > random_num:
            attempts += 1
            print ('Too high! Try lower: ')
        elif type(num) is str:
            print('See you next time.')
            flag = True
if __name__ == "__main__":
    guessingGame()

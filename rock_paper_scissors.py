#!/usr/bin/env/python3
def game():
    """
    by: gsilvapt
    Rock, Paper, Scissors game.
    The game will ask for a player input and will simulate a game.
    After 3 rounds, will ask if you wish to start again.
    (str) -> str
    """
    import random
    options = ['r', 'p', 's']
    runs = True
    while runs != False:
        opponent = random.choice(options)
        print(opponent) # Debugging purpose
        player_input = input("Rock (r), Paper (p) or Scissors (s)?" + \
                " (q to quit) ")
        if player_input == 'q':
            break
            runs = False
        elif player_input == 'r' and opponent == 's' or player_input == 'p' \
                and opponent == 'r' or player_input == 's' and opponent == 'p':
                    print('You Win! \n')
                    runs = False
                    retry = input("Do you wish to play again? (y or n) ")
                    if retry == 'y': 
                        runs = True
                    else:
                        runs = False
        elif player_input == 'r' and opponent == 'p' or player_input == 'p' \
                and opponent == 's' or player_input == 's' and opponent == 'r':
                    print("You lose! \n")
                    runs = False
                    retry = input ('Do you wish to play again? (y or n) ')
                    if retry == 'y':
                        runs = True
                    else:
                        runs = False
        elif player_input == opponent:
            print("It's a tie!")
            runs = False
            retry = input ('Do you wish to play again? (y or n) ')
            if retry == 'y':
                runs = True
            else:
                runs = False
if __name__ == '__main__':
    game()

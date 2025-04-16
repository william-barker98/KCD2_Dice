import const
import random
import time
from dice import Dice

p_points = 0    # player points
o_points = 0    # opponent points
t_points = 0   # number of points needed to win the game
first_player = 0

player_dice = []
opponent_dice = []

def welcome(t_points):


        print("Welcome! What should target score be?")
        time.sleep(1)
        while t_points == 0:
            choice = None
            print('''1. 1500
2. 3000
3. 4500.
4. Exit.''')
            choice = input("Choice: ")
            if choice == "1":
                t_points = 1500
            elif choice == "2":
                t_points = 3000
            elif choice == "3":
                t_points = 4500
            elif choice == "4":
                exit()
            else:
                print("Choice is invalid, please try again")



def setup():

    for i in range(const.NUMBER_OF_DICE):
        player_dice.append(Dice(i+1))
        opponent_dice.append(Dice(i+1))


def coin_flip(): # determine who goes first
    flip =  random.randint(0, 1)
    if flip == 0:
        print("You're going first!")
    else:
        print("Your opponent is going first!")
    first_player = int(flip)

def roll_dice():
    first_player = 0
    player_dice_rolled = []
    if first_player == 0: # if player goes first
        for die in player_dice:
            result = die.roll()
            print(die.id, "Rolled: {}".format(result))
            player_dice_rolled.append(result)
            print(player_dice_rolled)
    else:   # opponent turn
        pass


def find_consecutive_sequences(numbers):    # used to find every set of consecutive numbers from among the dice selected.
    if not numbers:
        return []

    sequences = []
    current_sequence = [numbers[0]]
    print(current_sequence)


    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1] + 1:
            current_sequence.append(numbers[i])
        else:
            if len(current_sequence) >= 4:
                sequences.append(current_sequence)
            current_sequence = [numbers[i]]

    if len(current_sequence) >= 4:
        sequences.append(current_sequence)

    return sequences

# Example usage
numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16]
print(find_consecutive_sequences(numbers))

welcome(t_points)
setup()
coin_flip()
roll_dice()



# Example usage


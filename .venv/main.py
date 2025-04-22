import const
import random
import time
from dice import Dice
from colorama import Fore, Style, init

# Initialize colorama
init()


p_points = 0    # player points
o_points = 0    # opponent points
t_points = 0   # number of points needed to win the game
first_player = 0    #  first player is 0, AI is 1
dice_count = const.NUMBER_OF_DICE   # the maximum number of dice both the player and AI start with.

temp_score = 0 # used to store the score while you're still playing a round. If you go bust, this resets and swaps to your opponent.
score = 0

player_dice = []    # both these lists are used to store the dice being rolled by the player and the AI.
opponent_dice = []


def find_consecutive_sequences(numbers):    # used to find every set of consecutive numbers from among the dice selected.
    if not numbers:
        return []
    numbers.sort()

    sequences = []
    current_sequence = [numbers[0]]



    for i in range(1, len(numbers)):

        if numbers[i] == numbers[i - 1] + 1: # if the number above in the list is one greater than the current number
            current_sequence.append(numbers[i])
        elif numbers[i] == numbers[i-1]: # if the number is the same
            pass
        else:   # if the 2 two numbers are not consecutive or not the same
            if len(current_sequence) >= 5:  # if we have a sequence of 4 or greater already
                sequences.append(current_sequence)  # add our current sequence to the list of sequences
            current_sequence = [numbers[i]]

    if len(current_sequence) >= 5:
        sequences.append(current_sequence)


    if not sequences:   # if sequences is empty
        pass
    else:   # otherwise
        pass
    return sequences
def welcome(t_points):  # will probably merge with the setup function, I probably don't need both.


        print("Welcome! What should target score be?")
        time.sleep(1)
        while t_points == 0:
            choice = None
            print('''1. 1500
2. 3000
3. 4500.
4. Exit.''')
            choice = input("Choice: ")  # The player chooses how many points either player needs to meet/surpass to win the game.
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



def setup():    # handles setting up the game.

    for i in range(const.NUMBER_OF_DICE):   #  populates each dice list with Dice objects, assigning each of them a number ID (1, 2, 3 etc).
        player_dice.append(Dice(i+1))
        opponent_dice.append(Dice(i+1))

    return player_dice, opponent_dice


def coin_flip(): # determine who goes first
    flip =  random.randint(0, 1)
    if flip == 0:
        print("You're going first!")
    else:
        print("Your opponent is going first!")
    first_player = int(flip)

def roll_dice(dice):
    first_player = 0    # testing with player always going first
    #i = 1
    if first_player == 0: # if player goes first
        for die in dice:
            #die.result = i
            #i+=1
            die.roll()

    else:   # opponent turn
        pass
    test_dice = [1,2,3,4,5,5]
    choose_dice(player_dice)



def choose_dice(dice):  # this function prints out each dice roll and allows the player to select the dice they wish to score.
    global temp_score
    global score
    num_dice = len(dice)    # stores how many dice either player has left to roll.
    chosen_pool = []    # stores the dice that the player/AI will choose to keep.
    choosing = True

    while choosing: # after choosing a die to keep, the list of rolled dice will refresh, allowing the player to choose the next die to keep.
        i = 1
        for die in dice:
            if die in chosen_pool:  # if the die has been chosen, it shall be highlighted in green.
                print("{}{}. {}".format(Fore.GREEN, i, die.result), Style.RESET_ALL)    #
            else:   # otherwise just prints the die out like normal.
                print("{}. {}".format(i, die.result))
            i+=1
        print("z. Commit and continue")
        print("x. Commit and pass")

        choice = input("Press the corresponding dice number to add/remove it to/from your pool:")
        if choice.isdigit():    # checks that the input from the player is a number. This is important because we use the number chosen as an index later and if the value isn't numerical, there will be an error.
            choice = int(choice)    # converts the string to an int.
            try:
                if dice[choice-1] in chosen_pool:
                    chosen_pool.remove(dice[choice-1])
                else:
                    chosen_pool.append(dice[choice-1])
                score = check_score(chosen_pool)
                print("SCORE: {}".format(score))
            except:
                print("Invalid input. Try again.")
        else:
            if choice == "z":
                # choose and continue
                choosing = False
                for die in chosen_pool:
                    dice.remove(die)
                #num_dice -= len(chosen_pool)
                #print("len chosen_pool: {}".format(len(chosen_pool)))
                #print("num of dice: {}".format(num_dice))
                temp_score += score
                roll_dice(dice)
                pass
            elif choice == "x":
                # choose and pass
                pass
            else:
                print("Invalid input. Try again #2.")




def check_score(dice_pool): # once the player chooses the dice, this function is used to see how much the chosen dice score.
    dice_results = []
    score = 0
    consecutive_dice = []   # used to store a list of 5 or more consecutive dice.
    remaining_dice = [] # stores the dice that haven't been used to score already.
    test_consc = [1, 2, 3, 4, 5, 6]
    count_dict = {} # a dict used for scoring 3 or more of a kind; the key stores the number rolled on the dice and the value stores the number of times that number was rolled.
    for d in dice_pool:
        dice_results.append(d.result)   # populate the dice_results list with the result attribute of each Dice object passed to this function as a parameter (dice_pool).

    if len(dice_pool) > 4:  # only checks to see if there are 5 or more consecutive numbers if there are 5 or more dice rolled.
        consecutive_dice = find_consecutive_sequences(dice_results) # returns a if there are any consecutive, returns any # numbers that aren't consecutive to be scored seperately.
        if not consecutive_dice:    # if there are not 5 or more consecutive dice, skip this section.
            pass
        else:
            consecutive_dice = consecutive_dice[0]
            print("CONSCSC", consecutive_dice)
            print("Dice Results for straights", dice_results)
            for i in consecutive_dice:
                dice_results.remove(i)
    if not consecutive_dice:
        if len(dice_pool) >= 3:
            # counts how many of a kind there are
            for d in dice_results:
                if d in count_dict:
                    count_dict[d] += 1
                else:
                    count_dict[d] = 1
            print(count_dict)
            keys = count_dict.keys()
            values = count_dict.values()

            for key, value in count_dict.items():
                if value == 3:
                    if key == 1:
                        score += 1000
                    elif key == 2:
                        score += 200
                    elif key == 3:
                        score += 300
                    elif key == 4:
                        score += 400
                    elif key == 5:
                        score += 500
                    elif key == 6:
                        score += 600
                    for i in range(3):
                        dice_results.remove(key)



                elif value == 4:
                    if key == 1:
                        score += 2000
                    elif key == 2:
                        score += 400
                    elif key == 3:
                        score += 600
                    elif key == 4:
                        score += 800
                    elif key == 5:
                        score += 1000
                    elif key == 6:
                        score += 1200
                    for i in range(4):
                        dice_results.remove(key)

                elif value == 5:
                    if key == 1:
                        score += 4000
                    elif key == 2:
                        score += 800
                    elif key == 3:
                        score += 1200
                    elif key == 4:
                        score += 1600
                    elif key == 5:
                        score += 2000
                    elif key == 6:
                        score += 2400
                elif value == 6:
                    if key == 1:
                        score += 8000
                    elif key == 2:
                        score += 1600
                    elif key == 3:
                        score += 2400
                    elif key == 4:
                        score += 3200
                    elif key == 5:
                        score += 4000
                    elif key == 6:
                        score += 4800
                    for i in range(5):
                        dice_results.remove(key)


    else:
        if len(consecutive_dice) == 6:
            score += 1500
        elif len(consecutive_dice) == 5:
            if consecutive_dice == [1, 2, 3, 4, 5]:
                score += 500
            else:
                score += 750



    # now we score the dice that haven't been scored yet

    print("consec dice: {}".format(consecutive_dice))
    print("Dice Results, {}".format(dice_results))
    for r in dice_results:
        if r in dice_results:
            if r == 1:
                score += 100
            elif r == 5:
                score += 50
            else:
                pass


    return score



#welcome(t_points)
p_dice, o_dice = setup()
coin_flip()
print(len(p_dice))
roll_dice(p_dice)


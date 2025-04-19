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
first_player = 0
dice_count = const.NUMBER_OF_DICE

temp_score = 0 # used to store the score while you're still playing a round. If you go bust, this resets and swaps to your opponent.

player_dice = []
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
    first_player = 0    # testing with player always going first
    i = 1
    if first_player == 0: # if player goes first
        for die in player_dice:
            #die.result = i
            #i+=1
            die.roll()

    else:   # opponent turn
        pass
    test_dice = [1,2,3,4,5,5]
    choose_dice(player_dice)



def choose_dice(dice):
    i = 1
    chosen_pool = []
    choosing = True
    while choosing:
        i = 1
        for die in dice:
            if die in chosen_pool:
                print("{}{}. {}".format(Fore.GREEN, i, die.result), Style.RESET_ALL)
            else:
                print("{}. {}".format(i, die.result))
            i+=1
        print("z. Commit and continue")
        print("x. Commit and pass")

        choice = input("Press the corresponding dice number to add/remove it to/from your pool:")
        if choice.isdigit():
            choice = int(choice)
            #try:
            if dice[choice-1] in chosen_pool:
                chosen_pool.remove(dice[choice-1])
            else:
                chosen_pool.append(dice[choice-1])
            score = check_score(chosen_pool)
            print("SCORE: {}".format(score))
        #except:
            #print("Invalid input. Try again.")
        else:
            if choice == "z":
                # choose and continue
                player_dice -= len(chosen_pool)
                temp_score += score
                pass
            elif choice == "x":
                # choose and pass
                pass
            else:
                print("Invalid input. Try again #2.")




def check_score(dice_pool):
    dice_results = []
    score = 0
    consecutive_dice = []
    remaining_dice = []
    test_consc = [1, 2, 3, 4, 5, 6]
    duplicates = []
    count_dict = {}
    for d in dice_pool:
        dice_results.append(d.result)

    if len(dice_pool) > 4:
        consecutive_dice = find_consecutive_sequences(dice_results) # returns a if there are any consecutive, returns any # numbers that aren't consecutive to be scored seperately.
        if not consecutive_dice:
            pass
        else:
            consecutive_dice = consecutive_dice[0]
            print("CONSCSC", consecutive_dice)
            print("Dice Results for straights", dice_results)
            for i in consecutive_dice:
                dice_results.remove(i)
    if not consecutive_dice:
        if len(dice_pool) >= 3:
            # check how many of a kind there are
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
                    dice_results.remove(key)
                    dice_results.remove(key)
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
                        dice_results.remove(key)
                        dice_results.remove(key)
                        dice_results.remove(key)
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
                    dice_results.remove(key)
                    dice_results.remove(key)
                    dice_results.remove(key)
                    dice_results.remove(key)
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
setup()
coin_flip()
roll_dice()



# Example usage


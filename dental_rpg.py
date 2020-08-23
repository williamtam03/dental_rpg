##
# dental_rpg.py
# Created On: 18/08/20
# Program that educates young children on dental hygiene in an
# RPG Style
# V 0.1C

import time

def characters():
    """
    Creates the characters used in the game
    """
    my_char = "Toothbrush"
    enemy_char = "Plaque"
    return my_char, enemy_char


def main():
    """
    Welcomes users and calls the attacking function
    and everything else
    """
    total_time = 0
    print("Welcome to the dental RPG!")
    my_char, enemy_char = characters()
    print()
    total_time = turn(my_char, enemy_char, total_time)
    print("You took a total of {:.02}s to attack 5 times!".format(total_time))
    


def attacking(my_char):
    """
    Attacking function for user
    """
    time_taken = 0
    timer_start = time.perf_counter()
    attack = input("Press enter to attack: ").upper()
    timer_end = time.perf_counter()
    if attack == "":
        print("You: {} attacked".format(my_char))
    else:
        print("You did not attack, you missed the button")
    time_taken = timer_end - timer_start
    return time_taken

def turn(my_char, enemy_char, total_time):
    """
    Turn function that will allow charcter to attack turn after turn
    """
    for i in range (5):
        time_taken = attacking(my_char)
        print("The enemy: {} attacked back!\n".format(enemy_char))
        total_time += time_taken
    return total_time
        


main()

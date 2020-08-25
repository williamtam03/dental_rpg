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
    # Setting variables and welcoming user to the RPG
    total_time = 0
    print("Welcome to the dental RPG!")
    # Calling character, turn, and attack functions
    my_char, enemy_char = characters()
    print()
    total_time = turn(my_char, enemy_char, total_time)
    # Output time taken
    print("You took a total of {:.02}s to attack 5 times!".format(total_time))
    


def attacking(my_char):
    """
    Attacking function for user
    """
    # Define variables
    time_taken = 0
    # Start timer
    timer_start = time.perf_counter()
    attack = input("Press enter to attack: ").upper()
    # End timer after attack is finished
    timer_end = time.perf_counter()
    # If statements to valid check the attack
    if attack == "":
        print("You: {} attacked".format(my_char))
    else:
        print("You did not attack, you missed the button")
    # Calaculates time taken in the attack and returns it
    time_taken = timer_end - timer_start
    return time_taken


def turn(my_char, enemy_char, total_time):
    """
    Turn function that will allow charcter to attack turn after turn
    """
    # Creates a loop for the number of times to attack (temp)
    for i in range (5):
        time_taken = attacking(my_char)
        print("The enemy: {} attacked back!\n".format(enemy_char))
        # Calcs total time taken with each turn
        total_time += time_taken
    return total_time
        

main()

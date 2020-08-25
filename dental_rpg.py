##
# dental_rpg.py
# Created On: 18/08/20
# Program that educates young children on dental hygiene in an
# RPG Style
# V 0.2B

import time
import thread
import sys

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
    print("Welcome to the dental RPG!")
    print("""You have a total of 5 seconds per round to attack!
Otherwise you will miss!""")
    # Calling character, turn, and attack functions
    my_char, enemy_char = characters()
    print()
    # countdown()
    print()
    t1 = Thread(target=timer)
    t2 = Thread(target=attacking(my_char, enemy_char))
    t1.start()
    t2.start()
    # turn(t1, t2)



def timer():
    for i in range(5):
        time.sleep(1)   #waits 45 seconds
    print("5 sec up")


def attacking(my_char, enemy_char):
    """
    Attacking function for user
    """
    attack = input("Press enter to attack: ").upper()
    if attack == "":
        print("You: {} attacked".format(my_char))
    else:
        print("You did not attack, you missed the button")
    print("The enemy: {} attacked back!\n".format(enemy_char))


def turn(t1, t2):
    """
    Turn function that will allow charcter to attack turn after turn
    """
    
        


main()

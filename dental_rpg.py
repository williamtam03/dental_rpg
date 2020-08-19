##
# dental_rpg.py
# Created On: 18/08/20
# Program that educates young children on dental hygiene in an
# RPG Style
# V 0.1B

import time

def characters():
    my_char = "Toothbrush"
    enemy_char = "Plaque"
    return my_char, enemy_char


def main():
    print("Welcome to the dental RPG!")
    my_char, enemy_char = characters()
    print()
    turn(my_char, enemy_char)


def attacking(my_char):
    """
    Attacking function for user
    """
    print("You have 5 seconds to attack!")
    timer_start = time.perf_counter()
    attack = input("Press enter to attack: ").upper()
    timer_end = time.perf_counter()
    if attack == "" and (timer_end - timer_start) <= 5:
        print("You: {} attacked".format(my_char))
    elif (timer_end - timer_start) > 5:
        print("You did not attack, you took too long, {:.04}s"
              .format(timer_end - timer_start))
    else:
        print("You did not attack, you missed the button")


def turn(my_char, enemy_char):
    while True:
        attacking(my_char)
        print("The enemy: {} attacked back!\n".format(enemy_char))
        
        


main()

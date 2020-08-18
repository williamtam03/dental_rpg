##
# dental_rpg.py
# Created On: 18/08/20
# Program that educates young children on dental hygiene in an
# RPG Style
# V 0.1

import msvcrt

def characters():
    my_char = "Toothbrush"
    enemy_char = "Plaque"
    return my_char, enemy_char


def main():
    print("Welcome to the dental RPG!")
    my_char, enemy_char = characters()
    turn(my_char, enemy_char)


def attacking(my_char):
    attack = input("Press enter to attack: ").upper()
    if attack == "":
        print("You: {} attacked".format(my_char))
    else:
        print("You did not attack")

def turn(my_char, enemy_char):
    while True:
        attacking(my_char)
        print("The enemy: {} attacked back!".format(enemy_char))

main()

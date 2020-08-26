##
# dental_rpg.py
# Created On: 18/08/20
# Program that educates young children on dental hygiene in an
# RPG Style
# V 0.2.2C

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
    print("""You have 5 rounds to attack
You will be timed on how long it will take you to attack for the 5 rounds""")
    # Calling character, turn, and attack functions
    my_char, enemy_char = characters()
    print()
    countdown()
    print()
    total_time = turn(my_char, enemy_char, total_time)
    # Output time taken
    print("You took a total of {:.02f}s to get through 5 rounds!".format(total_time))


def countdown():
    """
    Timer to delay the start of the the attack function
    """
    t = 5
    # While loop that will set the timer and then count down
    while t: 
        timer = "{}s left... ".format(t) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print("Go!")


def attacking(my_char):
    """
    Attacking function for user
    """
    # Define variables
    time_taken = 0
    # Start timer
    timer_start = time.perf_counter()
    attack = input("Press enter to attack: ").upper()
    # End timer after attack is finished and calcs time taken
    timer_end = time.perf_counter()
    time_taken = timer_end - timer_start
    # Function that checks the attacks and time taken
    attack_dmg(attack, time_taken, my_char)
    # Calaculates time taken in the attack and returns it
    
    return time_taken

def attack_dmg(attack, time_taken, my_char):
    """
    Determines what damage attack has occured
    """
    # If statements with boundaries for different attack damages
    if attack == "" and time_taken <= 2:
        print("You: {} took {:.02f}s to attack, you attacked full damage!".format(my_char, time_taken))
    elif attack == "" and time_taken <= 5 and time_taken > 2:
        print("You: {} took {:.02f}s to attack, you attacked at 80% damage, you were too slow!".format(my_char, time_taken))
    elif attack == "" and time_taken > 5:
        print("You: {} took {:.02f}s to attack, you attacked at only 50% damage, you were too slow!".format(my_char, time_taken))
    else:
        print("You did not attack, you missed the button")


def turn(my_char, enemy_char, total_time):
    """
    Turn function that will allow charcter to attack turn after turn
    """
    # Creates a loop for the number of times to attack (temp)
    for i in range(5):
        # Tells the user the round number
        print("Round {}/5".format(i + 1))
        time_taken = attacking(my_char)
        print("The enemy: {} attacked back!\n".format(enemy_char))
        # Calcs total time taken with each turn
        total_time += time_taken
    return total_time
        

main()

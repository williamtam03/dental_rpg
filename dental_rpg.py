##
# dental_rpg.py
# Created On: 18/08/20
# Program that educates young children on dental hygiene in an
# RPG Style
# V 0.3

import time

def characters():
    """
    Creates the characters used in the game
    """
    name = input("\nWhat is your name?: ")
    my_char = [name, 100]
    enemy_char = ["Plaque", 100]
    return my_char, enemy_char


def main():
    """
    Welcomes users and calls the attacking function
    and everything else
    """
    # Setting variables and welcoming user to the RPG
    total_time = 0
    start = False
    print("Welcome to the dental RPG!")
    print("""You have 5 rounds to attack
You will be timed on how long it will take you to attack for the 5 rounds\n""")
    print("""Attack below 3s: 100% attack damage
Attack inbetween 3-5s: 80% attack damage
Attack over 5s: 50% attack damage""")
    
    # Calling character, turn, and attack functions
    my_char, enemy_char = characters()
    print()
    # Check if user is ready to start game by asking them to press enter
    # Will keep looping until starteed
    while start != "":
        start = input("Press enter to start: ")
    # Sets a countdown for the first round to begin
    print("Dental RPG will start in:")
    countdown(5)
    print()
    # Calcs time taken and outputs (speedrunning purposes)
    total_time = turn(my_char, enemy_char, total_time)
    print("You took a total of {:.02f}s to get through 5 rounds!".format(total_time))


def countdown(countdown_time):
    """
    Timer to delay the start of the the attack function
    """
    # defining variable for time to countdown
    # While loop that will set the timer and then count down
    while countdown_time:
        timer = "{}... ".format(countdown_time) 
        print(timer, end="\r") 
        time.sleep(1) 
        countdown_time -= 1
    print("\nGo!")


def attacking(my_char):
    """
    Attacking function for user
    """
    # Define variables
    time_taken = 0
    # Displays user the moveset
    print("What move would you like to do?")
    VALID_INPUT, MOVES = moves()
    # Asks user which move they want to do with error check
    choice = input("What would you like to do? {}: "
                   .format(VALID_INPUT)).upper().strip()
    while not(choice in VALID_INPUT):
        print("Please enter a valid input")
        print("")
        choice = input("What would you like to do? {}: "
                       .format(VALID_INPUT)).upper().strip()
        print("")
    # Timer countdown until the round starts
    print("Attack in:")
    countdown(3)
    # Start timer for damage and total time
    timer_start = time.perf_counter()
    for letter, action in MOVES.items():
        if choice in letter:
            attack = input("Press enter to {}: ".format(action[0])).upper()
            base_damage = action[1]
    print()
    # End timer after attack is finished and calcs time taken
    timer_end = time.perf_counter()
    time_taken = timer_end - timer_start
    # Function that checks the attacks and time taken
    damage = attack_dmg(attack, time_taken, my_char, base_damage)
    # Calaculates time taken in the attack and returns it
    
    return time_taken, damage


def moves():
    """
    The different moves each user can do
    """
    MOVES = {"A": ["Brush Teeth", 40], "B": ["Use Mouthwash", 40],
             "C": ["Floss", 40], "D": ["Stop eating bad food", 40]}
    for letter, action in sorted(MOVES.items()):
        print("({}) to {} - {}DMG".format(letter, action[0], action[1]))
    print("")

    VALID_INPUT = sorted(list(MOVES.keys()))
    
    return VALID_INPUT, MOVES
    

def attack_dmg(attack, time_taken, my_char, base_damage):
    """
    Determines what damage attack has occured
    """
    # If statements with boundaries for different attack damages
    if attack == "" and time_taken <= 2:
        damage = base_damage
        print("You: {} took {:.02f}s to attack, you dealt {}DMG!".format(my_char[0], time_taken, damage))
    elif attack == "" and time_taken <= 5 and time_taken > 2:
        damage = int(base_damage * 0.8)
        print("You: {} took {:.02f}s to attack, you dealt {}DMG, attack quicker!".format(my_char[0], time_taken, damage))
    elif attack == "" and time_taken > 5:
        damage = int(base_damage * 0.5)
        print("You: {} took {:.02f}s to attack, you dealt {}DMG, you were too slow!".format(my_char[0], time_taken, damage))
    else:
        print("You did not attack, you missed the button")

    return damage


def turn(my_char, enemy_char, total_time):
    """
    Turn function that will allow charcter to attack turn after turn
    """
    round = 1
    # Creates a loop for the number of times to attack (temp)
    while enemy_char[1] > 0:
        # Tells the user the round number and the health of each character
        print("Round {}\n".format(round))
        print("""You({}): \t\t Health: {}HP
{}: \t\t Health: {}HP\n""".
          format(my_char[0], my_char[1], enemy_char[0], enemy_char[1]))

        time_taken, damage = attacking(my_char)
        print("The enemy: {} attacked back!\n\n".format(enemy_char[0]))
        # Calcs total time taken with each turn
        total_time += time_taken
        enemy_char[1] -= damage
        round += 1
    return total_time
        

main()

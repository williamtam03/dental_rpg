##
# dental_rpg.py
# Created On: 18/08/20
# Program that educates young children on dental hygiene in an
# RPG Style
# V 0.3.1C

import time, random

def characters():
    """
    Creates the characters used in the game
    """
    name = input("\nWhat is your name?: ").title()
    my_char = [name, 100]
    enemy_chars = [["Plaque", 100], ["Bad Breath", 125], ["Gum Disease", 150]]
    return my_char, enemy_chars


def main():
    """
    Welcomes users and calls the turn function to begin the
    RPG based attacks
    """
    # Setting variables and welcoming user to the RPG
    total_time = 0
    total_rounds = 0
    total_round_time = 0
    MOVES = {"A": ["Brush Teeth", 40], "B": ["Use Mouthwash", 40],
             "C": ["Floss", 40], "D": ["Stop eating bad food", 40]}
    VALID_INPUT = sorted(list(MOVES.keys()))
    start = False

    # Welcoming the user and providing context to understand the game
    print("Welcome to the dental RPG!")
    print("""You will battle against 3 dental enemies!
If you beat all 3 you win!
Remember we will time you on how long it took you to beat the game and to attack!\n""")
    print("""------------------------------------------
ATTACK BUFFS:
Attack below 3s: 100% attack damage
Attack inbetween 3-5s: 80% attack damage
Attack over 5s: 50% attack damage
------------------------------------------""")
    
    # Calling character, turn, and attack functions
    my_char, enemy_chars = characters()
    print()

    # Acknowledge user input, tell them who they are up against today
    print("""Hello {}!\n
------------------------------------------
The enemies you are up against are:""".format(my_char[0]))
    for enemy_char in enemy_chars:
        print("{}: {}HP".format(enemy_char[0], enemy_char[1]))
    
    print("------------------------------------------\n")
    # Check if user is ready to start game by asking them to press enter
    # Will keep looping until starteed
    while start != "":
        start = input("Press enter to start: ")
    # Sets a countdown for the first round to begin
    print("Dental RPG will start in:")
    
    # countdown(5)
    print()
    # Calcs time taken and outputs (speedrunning purposes)
    for enemy_char in enemy_chars:
        total_round_time, round, win = turn(my_char, enemy_char, total_round_time, MOVES, VALID_INPUT)
        total_rounds += round
        total_time += total_round_time
        if win == False:
            print("""\n⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿""")
            print("You lost! You took a total of {:.02f}s and lasted {} rounds!".format(total_time, total_rounds))
            break
    if win == True:
        print("You took a total of {:.02f}s and bet the game in {} rounds!".format(total_time, total_rounds))
    


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


def attacking_user(my_char, MOVES, VALID_INPUT):
    """
    Attacking function for user
    """
    # Displays user the moveset
    round_start = time.perf_counter()
    print("What move would you like to do?")
    for letter, action in sorted(MOVES.items()):
        print("({}) to {} - {}DMG".format(letter, action[0], action[1]))
    print("")
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
    print("""NOTE:
To attack, select the correct answer""")
    print("Attack in:")
    
    # countdown(3)
    print()

    
    # Start timer for damage and total time
    attack_start = time.perf_counter()
    for letter, action in MOVES.items():
        if choice in letter:
            attack = trivia(choice)
            base_damage = action[1]
    # 5% randomised miss rate
    attack = randomised_miss(attack)
    # End timer after attack is finished and calcs attack time and round time
    timer_end = time.perf_counter()
    attack_time =  timer_end - attack_start
    round_time = timer_end - round_start
    # Function that checks the attacks and time taken
    damage = attack_dmg(attack, attack_time, my_char, base_damage)
    
    return round_time, damage


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer


def trivia(choice):
    """
    Trivia function for questions that will be asked in the function
    """
    keys = ["A", "B", "C", "D"]
    trivia_prompts = ["""What is the optimal time to brush teeth for?:\n{0}: 1 Minute
{1}: 30 Seconds\n{2}: 2 Minutes\n{3}: 1 and a half Minutes\n""".format(*keys),
                      """How often should you brush your teeth?:\n{0}: Twice a day
{1}: Once a day\n{2}: Every 2 days\n{3}: Three times a day\n""".format(*keys),
                      
                      """What is the optimal time to rinse with mouthwash?:\n{0}: 1 Minute
{1}: 30 Seconds\n{2}: 2 Minutes\n{3}: 1 and a half Minutes\n""".format(*keys),
                      """How should you use mouthwash?:\n{0}: Light Swish
{1}: Light Gargle\n{2}: Swish Vigorously and Gargle\n{3}: Swish Vigorously\n""".format(*keys),

                      """What is the optimal length to floss with?:\n{0}: 10cm
{1}: 25cm\n{2}: 60cm\n{3}: 45cm\n""".format(*keys),
                      """How often should you floss your teeth?:\n{0}: Once a day
{1}: Twice a day\n{2}: Every 2 days\n{3}: Three times a day\n""".format(*keys)]

    brush_questions = [
        Question(trivia_prompts[0], "C"),
        Question(trivia_prompts[1], "A")]
    
    mouthwash_questions = [
        Question(trivia_prompts[2], "B"),
        Question(trivia_prompts[3], "C")]

    floss_questions = [
        Question(trivia_prompts[4], "D"),
        Question(trivia_prompts[5], "A")]

    if choice == "A":
        attack = run_quiz(brush_questions)
    elif choice == "B":
        attack = run_quiz(mouthwash_questions)
    elif choice == "C":
        attack = run_quiz(floss_questions)

    print(attack)

    return attack


def run_quiz(questions):
    """
    Runs the quiz for the questions and answers
    """
    q_set = random.randint(0,1)
    print(q_set)
    question = questions[q_set]
    answer = input(question.prompt).upper()
    if answer == question.answer:
        attack = True
    else:
        attack = False
    return attack
   
        

def attacking_bot(enemy_char, MOVES, VALID_INPUT):
    letter_sequence = ""
    choice = VALID_INPUT[random.randint(0, 3)]
    attack = True
    attack = randomised_miss(attack)
    # Randomised attack time for bot
    attack_time = random.uniform(0, 6)
    # Set base damage for enemy
    base_damage = 30
    print("The enemy is attacking...")
    time.sleep(1.5)
    damage = attack_dmg(attack, attack_time, enemy_char, base_damage)
    return damage


def randomised_miss(attack):
    hit_rate = random.randint(1, 20)
    if hit_rate == 6:
        attack = False
        
    return attack
    print()


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
    

def attack_dmg(attack, attack_time, character, base_damage):
    """
    Determines what damage attack has occured
    """
    VALID_ATTACK = True
    # If statements with boundaries for different attack damages
    if attack == VALID_ATTACK and attack_time <= 2:
        damage = base_damage
        print("{} took {:.02f}s to attack, and dealt {}DMG!".format(character[0], attack_time, damage))
    elif attack == VALID_ATTACK and attack_time <= 5 and attack_time > 2:
        damage = int(base_damage * 0.8)
        print("{} took {:.02f}s to attack, and dealt {}DMG!".format(character[0], attack_time, damage))
    elif attack == VALID_ATTACK and attack_time > 5:
        damage = int(base_damage * 0.5)
        print("{} took {:.02f}s to attack, and dealt {}DMG!".format(character[0], attack_time, damage))
    else:
        print("{0} did not attack, {0} missed!".format(character[0]))
        damage = 0

    return damage


def turn(my_char, enemy_char, total_round_time, MOVES, VALID_INPUT):
    """
    Turn function that will allow charcter to attack turn after turn
    """
    round = 1
    win = True
    # Creates a loop for the number of times to attack (temp)
    while enemy_char[1] > 0:
        # Tells the user the round number and the health of each character
        print("\u0332".join("Round {}".format(round)))
        print("""------------------------------------------
You({}): \t\t Health: {}HP
{}: \t\t Health: {}HP
------------------------------------------\n""".
          format(my_char[0], my_char[1], enemy_char[0], enemy_char[1]))

        # Calls on user and enemy attack functions
        round_time, user_damage = attacking_user(my_char, MOVES, VALID_INPUT)
        enemy_char[1] -= user_damage
        total_round_time += round_time
        if enemy_char[1] <= 0:
            
            break
        print()
        enemy_damage = attacking_bot(enemy_char, MOVES, VALID_INPUT)
        my_char[1] -= enemy_damage
        if my_char[1] <= 0:
            win = False
            break
        print()
        # Calculates total time taken with each turn
        round += 1
    return total_round_time, round, win


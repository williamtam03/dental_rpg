##
# dental_rpg.py
# Created On: 18/08/20
# Program that educates young children on dental hygiene in an
# RPG Style
# V 0.3.2


import time, random


def force_number(message):
    """
    Uses try and except to ensure
    variable entered is a number and wont error out
    """
    while True:
        try:
            number = int(input(message))
            break
        except ValueError:
            print("Please enter a number!")
    return number


def characters():
    """
    Creates the characters used in the game
    """
    MAX_CHARS = 35
    name = input("\nWhat is your name?: ").title().strip()
    while name == "" or len(name) > MAX_CHARS:
        print("Please enter a name!")
        name = input("What is your name?: ").title()
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
    VALID_INPUT, MOVES = moves()
    NAME = 0
    HEALTH = 1
    start = False

    # Welcoming the user and providing context to understand the game
    print("Welcome to the dental RPG!")
    print("""You will battle against 3 dental enemies!
If you beat all 3 you win!
Remember we will time you on how long it
took you to beat the game and to attack!
So try your hardest to be quick!!!\n""")
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
The enemies you are up against are:""".format(my_char[NAME]))
    for enemy_char in enemy_chars:
        print("{}: {}HP".format(enemy_char[NAME], enemy_char[HEALTH]))
    
    print("------------------------------------------\n")
    # Check if user is ready to start game by asking them to press enter
    # Will keep looping until starteed
    while start != "":
        start = input("Press enter to start: ")
    # Sets a countdown for the first round to begin
    print()
    my_char_intial_health = my_char[HEALTH]
    # Calcs time taken and outputs (speedrunning purposes)
    for enemy_char in enemy_chars:
        # countdown(5, "Next round starts in: ")
        total_round_time, round, win = turn(my_char, my_char_intial_health, enemy_char, total_round_time, MOVES, VALID_INPUT, NAME, HEALTH)
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
        print("""\n⠄⠄⠄⠄⠄⠄⣀⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣿⣿⣿⣶⣦⣄⠄⠄
⠄⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦
⢠⠾⣋⣭⣄⡀⠄⠄⠈⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⡎⣾⡟⢻⣿⣷⠄⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⣿⣿
⡇⢿⣷⣾⣿⠟⠄⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼⣿⣿⣿⣿
⢸⣦⣭⣭⣄⣤⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿⣿⣿⣿⣿
⠄⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢰⡿⠛⠛⠛⠛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠸⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠈⣆⠄⠄⢿⣿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⣿⠁⠄⠐⠛⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⠄⠄⠻⣦⣀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄""")
        print("You took a total of {:.02f}s and bet the game in {} rounds!".format(total_time, total_rounds))
    


def countdown(countdown_time, message):
    """
    Timer to delay the start of the the attack function
    """
    # defining variable for time to countdown
    # While loop that will set the timer and then count down
    print(message)
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
    choice = 0
    ACTION_NAME = 0
    DMG = 1
    # Displays user the moveset
    round_start = time.perf_counter()
    print("What move would you like to do?")
    for letter, action in sorted(MOVES.items()):
        print("({}) to {} - {}DMG".format(letter, action[ACTION_NAME], action[DMG]))
    print("")
    # Asks user which move they want to do with error check
    while not(choice in VALID_INPUT):
        choice = force_number(("What would you like to do? {}: "
                   .format(VALID_INPUT)))
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
        if choice == letter:
            attack = trivia(choice)
            base_damage = action[DMG]
    # 5% randomised miss rate
    attack = randomised_miss(attack)
    # End timer after attack is finished and calcs attack time and round time
    timer_end = time.perf_counter()
    attack_time =  timer_end - attack_start
    round_time = timer_end - round_start
    # Function that checks the attacks and time taken
    damage = attack_dmg(attack, attack_time, my_char, base_damage)
    
    return round_time, damage


class question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer


def trivia(choice):
    """
    Trivia function for questions that will be asked in the function
    """
    # Set keys for each answer
    KEYS = [1, 2, 3, 4]
    trivia_prompts = []
    correct_answers = []

    question_sets = [["What is the optimal time to brush teeth for?: ", ["1 Minute", False], ["30 Seconds", False], ["2 Minutes", True], ["1 and a half Minutes", False]],
     ["How often should you brush your teeth?: ", ["Twice a day", True], ["Once a day", False], ["Every 2 days", False], ["Three times a day", False]],

     ["What is the optimal time to rinse with mouthwash?: ", ["1 Minute", False], ["30 Seconds", True], ["2 Minutes", False], ["1 and a half Minutes", False]],
     ["How should you use mouthwash?: ", ["Light Swish", False], ["Light Gargle", False], ["Swish Vigorously and Gargle", True], ["Swish Vigorously", False]],

     ["What is the optimal length to floss with?: ", ["10cm", False], ["25cm", False], ["60cm", False], ["45cn", True]],
     ["How often should you floss your teeth?: ", ["Twice a day", False], ["Once a day", True], ["Every 2 days", False], ["Three times a day", False]]]
    
    for question_set in question_sets:
        prompts, ans = prompt_shuffler(question_set, KEYS)
        trivia_prompts.append(prompts)
        correct_answers.append(ans)

# Set the questions into their own lists with the correct ans
    brush_questions = [
        question(trivia_prompts[0], correct_answers[0]),
        question(trivia_prompts[1], correct_answers[1])]
    
    mouthwash_questions = [
        question(trivia_prompts[2], correct_answers[2]),
        question(trivia_prompts[3], correct_answers[3])]

    floss_questions = [
        question(trivia_prompts[4], correct_answers[4]),
        question(trivia_prompts[5], correct_answers[5])]

# Runs the questions based on choice
    if choice == 1:
        attack = run_quiz(brush_questions, KEYS)
    elif choice == 2:
        attack = run_quiz(mouthwash_questions, KEYS)
    elif choice == 3:
        attack = run_quiz(floss_questions, KEYS)

    return attack


def prompt_shuffler(question_set, KEYS): 
    questions = []
    shuffle_set = question_set[1:]
    random.shuffle(shuffle_set)
    question_set[1:] = shuffle_set
    
    for i in range(len(KEYS)):
        question = ("{}: {}".format(KEYS[i], (question_set[i+1])[0]))
        if (question_set[i+1])[1] == True:
            ans = KEYS[i]
        questions.append(question)
        
    prompts = ("""{}
{}
{}
{}
{}
""".format(question_set[0], *questions))
    return prompts, ans


def run_quiz(questions, KEYS):
    """
    Runs the quiz for the questions and answers
    """
    # Randomises the question set from either
    q_set = random.randint(0,1)
    question = questions[q_set]
    # Asks user for ans and then checks if valid
    while True:
        try:
            answer = int(input(question.prompt).upper())
            break
        except ValueError:
            print("Please enter a valid input")
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
    MOVES = {1: ["Brush Teeth", 40], 2: ["Use Mouthwash", 40],
             3: ["Floss", 40], 4: ["Stop eating bad food", 40]}
    VALID_INPUT = sorted(list(MOVES.keys()))
    
    return VALID_INPUT, MOVES
    

def attack_dmg(attack, attack_time, character, base_damage):
    """
    Determines what damage attack has occured
    """
    VALID_ATTACK = True
    QUICK= 2
    MEDIUM= 5
    MED_MULTI = 0.75
    SLOW_MULTI = 0.5
    # If statements with boundaries for different attack damages
    if attack == VALID_ATTACK and attack_time <= QUICK:
        damage = base_damage
        print("{} took {:.02f}s to attack, and dealt {} DMG!".format(character[0], attack_time, damage))
    elif attack == VALID_ATTACK and attack_time <= MEDIUM and attack_time > QUICK:
        damage = int(base_damage * MED_MULTI)
        print("{} took {:.02f}s to attack, and dealt {} DMG!".format(character[0], attack_time, damage))
    elif attack == VALID_ATTACK and attack_time > MEDIUM:
        damage = int(base_damage * SLOW_MULTI)
        print("{} took {:.02f}s to attack, and dealt {} DMG!".format(character[0], attack_time, damage))
    else:
        print("{0} did not attack, {0} missed!".format(character[0]))
        damage = 0

    return damage


def turn(my_char, my_char_intial_health, enemy_char, total_round_time, MOVES, VALID_INPUT, NAME, HEALTH):
    """
    Turn function that will allow charcter to attack turn after turn
    """
    round = 1
    win = True
    NO_HEALTH = 0
    enemy_char_inital_health = enemy_char[HEALTH]
    # Creates a loop for the number of times to attack (temp)
    while enemy_char[HEALTH] > NO_HEALTH:
        # Tells the user the round number and the health of each character
        print("\u0332".join("Round {}".format(round)))
        print("""------------------------------------------
You({}): \t\t Health: {}/{}HP
{}: \t\t Health: {}/{}HP
------------------------------------------\n""".
          format(my_char[NAME], my_char[HEALTH], my_char_intial_health, enemy_char[NAME], enemy_char[HEALTH], enemy_char_inital_health))

        # Calls on user and enemy attack functions
        round_time, user_damage = attacking_user(my_char, MOVES, VALID_INPUT)
        
        enemy_char[HEALTH] -= user_damage
        total_round_time += round_time
        
        if enemy_char[1] <= NO_HEALTH:
            print("""░░░░░▒░░▄██▄░▒░░░░░░ 
░░░▄██████████▄▒▒░░░ 
░▒▄████████████▓▓▒░░ 
▓███▓▓█████▀▀████▒░░ 
▄███████▀▀▒░░░░▀█▒░░ 
████████▄░░░░░░░▀▄░░ 
▀██████▀░░▄▀▀▄░░▄█▒░ 
░█████▀░░░░▄▄░░▒▄▀░░ 
░█▒▒██░░░░▀▄█░░▒▄█░░ 
░█░▓▒█▄░░░░░░░░░▒▓░░ 
░▀▄░░▀▀░▒░░░░░▄▄░▒░░ 
░░█▒▒▒▒▒▒▒▒▒░░░░▒░░░ 
░░░▓▒▒▒▒▒░▒▒▄██▀░░░░ 
░░░░▓▒▒▒░▒▒░▓▀▀▒░░░░ 
░░░░░▓▓▒▒░▒░░▓▓░░░░░ 
░░░░░░░▒▒▒▒▒▒▒░░░░░░\n
You beat {}!\n""".format(enemy_char[NAME]))
            break
        print()
        enemy_damage = attacking_bot(enemy_char, MOVES, VALID_INPUT)
        my_char[1] -= enemy_damage
        if my_char[HEALTH] <= NO_HEALTH:
            win = False
            break
        print()
        # Calculates total time taken with each turn
        round += 1
    return total_round_time, round, win


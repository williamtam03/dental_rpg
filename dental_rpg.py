##
# dental_rpg.py
# Created On: 18/08/20
# Program that educates young children on dental hygiene in an
# RPG Style
# V 0.4


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
            print("Please enter a valid input!")
    return number


def characters(username, NAME, HEALTH):
    """
    Creates the characters used in the game
    """
    # Creates char and enemy for use in game
    my_char = [username, ["❤","❤","❤","❤","❤","❤","❤","❤","❤","❤"]]
    enemy_chars = [["Plaque", ["❤","❤","❤","❤","❤","❤","❤","❤","❤","❤"]],
                   ["Bad Breath", ["❤","❤","❤","❤","❤","❤","❤","❤","❤","❤","❤","❤"]],
                   ["Gum Disease", ["❤","❤","❤","❤","❤","❤","❤","❤","❤","❤","❤","❤","❤","❤","❤"]]]

    # Acknowledge user input, tell them who they are up against today
    print("""\n------------------------------------------
The enemies you are up against are:""")
    for enemy_char in enemy_chars:
        print("{}: {}".format(enemy_char[NAME], ''.join(enemy_char[HEALTH])))
    
    print("------------------------------------------\n")
    
    return my_char, enemy_chars


def menu(start_replay):
    choice = 0
    MENU = {1: start_replay, 2: "High Scores", 3: "Quit"}
    VALID_INPUT = sorted(list(MENU.keys()))
    for number, description in sorted(MENU.items()):
        print("({}) to {}".format(number, description))
    print("")

    # Asks for input then compares to see if valid or not
    # if not will ask again
    while not(choice in VALID_INPUT):
        choice = force_number(("What would you like to do? {}: "
                   .format(VALID_INPUT)))
        if choice in VALID_INPUT:
            break
        print("Please enter a number between 1 and 3!\n")

    return choice
    


def main():
    """
    Welcomes users and calls the turn function to begin the
    RPG based attacks
    """
    # Setting variables and constants
    total_time = 0
    total_rounds = 0
    total_round_time = 0
    VALID_INPUT, MOVES = moves()
    NAME = 0
    HEALTH = 1
    MAX_CHARS = 35
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
    
    username = input("\nWhat is your name?: ").title().strip()
    while username == "" or len(username) > MAX_CHARS:
        print("Please enter a name!")
        username = input("What is your name?: ").title()
    print("Hello {}!".format(username))
    print()
    choice = menu("Start Game")
    
    # Error check and loop to ensure user is ready to start
    while choice != 3:
        if choice == 1:
            # Calling characters to get name, and setting users initial health
            my_char, enemy_chars = characters(username, NAME, HEALTH)
            my_char_intial_health = my_char[HEALTH]
            print()
            
            # Loop through so user will fight all 3 enemies
            while start != "":
                start = input("Press enter to start: ")
            for enemy_char in enemy_chars:
                countdown(1, "Next round starts in: ")
                total_round_time, round, win = turn(my_char, my_char_intial_health, enemy_char, total_round_time, MOVES, VALID_INPUT, NAME, HEALTH)

                # Calcs total rounds and time taken(speedrunning purposes)
                total_rounds += round
                total_time += total_round_time
                
                # If statements telling user whether they won or lost
                # With info of total rounds and time taken
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

            choice = menu("Replay")
    

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
    # Setting vars and constants to be used in attack
    choice = 0
    ACTION_NAME = 0
    DMG = 1
    
    # Starts the timer for the round
    # and displays user the moveset for choice
    round_start = time.perf_counter()
    print("What move would you like to do?")
    for letter, action in sorted(MOVES.items()):
        print("({}) to {} - {}DMG".format(letter, action[ACTION_NAME], action[DMG]))
    print("")
    # Asks user which move they want to do with error check
    # and aknowledges user selection
    while not(choice in VALID_INPUT):
        choice = force_number(("What would you like to do? {}: "
                   .format(VALID_INPUT)))
        if choice in VALID_INPUT:
            break
        print("Please enter a number between 1 and 4\n")
    print("You selected {}!".format((MOVES[choice])[ACTION_NAME]))
    
    # Timer countdown until trivia will start, gives user time to prepare
    # countdown(3)
    print()
    
    # Start timer for the trivia begins it
    attack_start = time.perf_counter()
    for number, action in MOVES.items():
        if choice == number:
            attack = trivia(choice)
            base_damage = action[DMG]
    # 5% randomised miss rate
    attack = randomised_miss(attack)
    # End timer after attack is finished and calcs attack time and round time
    timer_end = time.perf_counter()
    attack_time =  timer_end - attack_start
    round_time = timer_end - round_start
    
    # Function that returns damage based on attack and time
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

    # Toothbrush Q
    question_sets = [["What is the optimal time to brush teeth for?: ", ["1 Minute", False], ["30 Seconds", False], ["2 Minutes", True], ["1 and a half Minutes", False]],
     ["How often should you brush your teeth?: ", ["Twice a day", True], ["Once a day", False], ["Every 2 days", False], ["Three times a day", False]],
    # Mouthwash Q
     ["What is the optimal time to rinse with mouthwash?: ", ["1 Minute", False], ["30 Seconds", True], ["2 Minutes", False], ["1 and a half Minutes", False]],
     ["How should you use mouthwash?: ", ["Light Swish", False], ["Light Gargle", False], ["Swish Vigorously and Gargle", True], ["Swish Vigorously", False]],
    # Floss Q
     ["What is the optimal length to floss with?: ", ["10cm", False], ["25cm", False], ["60cm", False], ["45cn", True]],
     ["How often should you floss your teeth?: ", ["Twice a day", False], ["Once a day", True], ["Every 2 days", False], ["Three times a day", False]]]

    # Iterate through list to turn it into a string that is readable
    # and has the correct ans
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

# Runs the questions based on the attack choice
    if choice == 1:
        attack = run_quiz(brush_questions, KEYS)
    elif choice == 2:
        attack = run_quiz(mouthwash_questions, KEYS)
    elif choice == 3:
        attack = run_quiz(floss_questions, KEYS)

    return attack


def prompt_shuffler(question_set, KEYS):
    """
    Shuffles the answers into random orders so user cant predict
    correct ans is 1 etc
    """
    # Setting empty list to turn into string that will be printed for prompt
    questions = []
    # Copy 4 answers to shuffle, then remakes the question set with shuffled ans
    shuffle_set = question_set[1:]
    random.shuffle(shuffle_set)
    question_set[1:] = shuffle_set

    # Iterates through keys to create the answer matched with key
    # i.e 1: 2 minutes
    for i in range(len(KEYS)):
        question = ("{}: {}".format(KEYS[i], (question_set[i+1])[0]))
        if (question_set[i+1])[1] == True:
            ans = KEYS[i]
        # Appends to list so it can be iterated through for string
        questions.append(question)

    # Creates the string user will see
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
    answer = 0
    # Randomises the question set from either
    q_set = random.randint(0,1)
    question = questions[q_set]
    # Asks user for ans and then checks if valid
    while not(answer in KEYS):
        answer = force_number("{}\nAnswer Here: ".format(question.prompt))
        if answer in KEYS:
            break
        print("Please enter a number betweeen 1 and 4\n")
    if answer == question.answer:
        attack = True
    else:
        attack = False
    return attack


def attacking_bot(enemy_char, MOVES, VALID_INPUT):
    """
    Bot that will attack for the enemy
    """
    # Predetermined vars for enemy attack
    base_damage = 3
    attack = True
    # Randomised miss and attack time for bot
    attack = randomised_miss(attack)
    attack_time = random.uniform(0, 6)

    # Lets user know the enemy is attacking and "thinking"
    print("The enemy is attacking...")
    time.sleep(1.5)
    
    damage = attack_dmg(attack, attack_time, enemy_char, base_damage)
    return damage


def randomised_miss(attack):
    """
    Randomises whether the attack will hit or not
    """
    # Randomises a number and if it matches selected num
    # Will miss (5% miss rate)
    hit_rate = random.randint(1, 20)
    miss_number = random.randint(1, 20)
    if hit_rate == miss_number:
        attack = False
        
    return attack
    print()


def moves():
    """
    The different moves each user can do
    """
    MOVES = {1: ["Brush Teeth", 4], 2: ["Use Mouthwash", 4],
             3: ["Floss", 4], 4: ["Stop eating bad food", 4]}
    VALID_INPUT = sorted(list(MOVES.keys()))
    
    return VALID_INPUT, MOVES
    

def attack_dmg(attack, attack_time, character, base_damage):
    """
    Determines what damage attack has occured
    """
    VALID_ATTACK = True
    QUICK = 2
    MEDIUM = 5
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
    # Defining variables and constants that will be used later
    round = 1
    win = True
    NO_HEALTH = 0
    enemy_char_inital_health = enemy_char[HEALTH]
    # Creates a loop for the number of times to attack (temp)
    while len(enemy_char[HEALTH]) > NO_HEALTH:
        my_char_hearts = ''.join(my_char[1])
        enemy_char_hearts = ''.join(enemy_char[1])
        # Tells the user the round number and the health of each character
        print("\u0332".join("Round {}".format(round)))
        print("""------------------------------------------
You({}): \t\t Health: {}
{}: \t\t Health: {}
------------------------------------------\n""".
          format(my_char[NAME], my_char_hearts, enemy_char[NAME], enemy_char_hearts))

        # Calls on user attack functions, then decreases health accordingly
        round_time, user_damage = attacking_user(my_char, MOVES, VALID_INPUT)

        while user_damage > 0:
            try:
                enemy_char[HEALTH].pop()
                user_damage -= 1
            except:
                break
        
        total_round_time += round_time

        # Tells user if they beat the enemy
        if len(enemy_char[HEALTH]) <= NO_HEALTH:
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
        
        # Calls on enemy attack functions, then decreases health accordingly
        enemy_damage = attacking_bot(enemy_char, MOVES, VALID_INPUT)
        while enemy_damage > 0:
            try:
                my_char[1].pop()
                enemy_damage -= 1
            except:
                break
        # Sets win to false to tell user that they lost
        if len(my_char[HEALTH]) <= NO_HEALTH:
            win = False
            break
        print()
        round += 1
    return total_round_time, round, win

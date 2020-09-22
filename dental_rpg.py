##
# dental_rpg.py
# Created On: 18/08/20
# Program that educates young children on dental hygiene in an
# RPG Style
# V 0.4.3


import time
import random


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
    my_char = [username, ["❤", "❤", "❤", "❤", "❤", "❤", "❤", "❤", "❤", "❤"]]
    enemy_chars = [["Plaque/Tohu", ["❤", "❤", "❤", "❤", "❤", "❤",
                                    "❤", "❤", "❤", "❤"]],
                   ["Bad Breath/Manawa Kino", ["❤", "❤", "❤", "❤", "❤", "❤",
                                               "❤", "❤", "❤", "❤", "❤", "❤"]],
                   ["Gum Disease/Mate Kapia", ["❤", "❤", "❤", "❤", "❤",
                                               "❤", "❤", "❤", "❤", "❤",
                                               "❤", "❤", "❤",
                                               "❤", "❤"]]]

    # Acknowledge user input, tell them who they are up against today
    print("""\n------------------------------------------
The enemies you are up against are:""")
    for enemy_char in enemy_chars:
        print("{}: {}".format(enemy_char[NAME], ''.join(enemy_char[HEALTH])))

    print("------------------------------------------\n")

    return my_char, enemy_chars


def moves():
    """
    The different moves each user can do
    """
    MOVES = {1: ["Brush Teeth/Nga niho paraihe       ", 4],
             2: ["Use Mouthwash/Whakamahia te Mutu Horoi", 4],
             3: ["Floss/Miro\t\t\t", 4],
             4: ["Dental Visit/Toro Niho\t\t", 3]}
    VALID_INPUT = sorted(list(MOVES.keys()))

    return VALID_INPUT, MOVES


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


def history_write(username, win, enemies_beaten, total_time):
    history_file = open("history.txt", "a")
    stat = [username, str(win), str(enemies_beaten), str(total_time)]
    stats = ", ".join(stat)
    history_file.write("{}\n".format(stats))
    history_file.close()


def history_print():
    """
    Highscore file opener
    """
    # Defining variable to be used later
    stat_list = []
    # Opens file and converts each line into a list
    # Then appends to a total list
    history_file = open("history.txt", "r")
    for stats in history_file:
        stats = stats.split(", ")
        stat_list.append(stats)
    history_file.close()

    # Calling sorter that sorts the results
    sorted_stats = stat_sorter(stat_list)

    # Tells user the top 10 highscores like requested
    print("Top 10 Highscores:\n")
    print("Name:\t\tWin:\t\tEnemies Beaten:\t\tTime Taken:")
    print("-------------------------------"
          "---------------------------------------")
    for stat in sorted_stats[:10]:
        print("{}\t\t{}\t\t{}\t\t\t{}s".format(*stat))
    print("-------------------------------"
          "---------------------------------------")


def custom_sort(t):
    """
    Sets the sort to be based of time
    """
    TOTAL_TIME = 1
    return t[TOTAL_TIME]


def stat_sorter(stat_list):
    """
    Sorts the stats based of win, round and time taken
    """
    # Defining variables for each category
    WIN = 1
    ENEMIES_BEAT = 2
    TOTAL_TIME = 3
    win = []
    r3_death = []
    r2_death = []
    r1_death = []

    # For loop to iterate through each players results in the game
    for stat in range(len(stat_list)):
        # Converts string literals to int and floats to make it easier
        (stat_list[stat])[ENEMIES_BEAT] = int((stat_list[stat])[ENEMIES_BEAT])
        (stat_list[stat])[TOTAL_TIME] = float(
            ((stat_list[stat])[TOTAL_TIME])[:5])
        # If statements to see where each player result falls into
        # Then categorises them
        if (stat_list[stat])[WIN] == "True":
            win.append(stat_list[stat])
            continue
        elif (stat_list[stat])[ENEMIES_BEAT] == 2:
            r3_death.append(stat_list[stat])
            continue
        elif (stat_list[stat])[ENEMIES_BEAT] == 1:
            r2_death.append(stat_list[stat])
            continue
        else:
            r1_death.append(stat_list[stat])

    # Sorts each category by time
    win = time_sorter(win)
    r3_death = time_sorter(r3_death)
    r2_death = time_sorter(r2_death)
    r1_death = time_sorter(r1_death)

    # Returns a list in order of time and how far they have gone descending
    sorted_stats = win + r3_death + r2_death + r1_death
    return sorted_stats


def time_sorter(stats):
    """
    Checks time taken for history
    """
    # Sorts by time
    stats.sort(key=custom_sort)
    return stats


def menu(start_replay):
    """
    Tells user options they have
    """
    choice = 0
    MENU = {1: start_replay,
            2: "Check High Scores/Tirohia Nga Kaute Teitei",
            3: "Quit/Whakamutu"}
    VALID_INPUT = sorted(list(MENU.keys()))
    # Tells the user the options they have
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


def turn(my_char, my_char_intial_health, enemy_char,
         total_round_time, MOVES, VALID_INPUT, NAME, HEALTH):
    """
    Turn function that will allow charcter to attack turn after turn
    """
    # Defining variables and constants that will be used later
    round = 1
    win = True
    NO_HEALTH = 0
    enemy_beaten = False
    enemy_char_inital_health = enemy_char[HEALTH]
    # Creates a loop for the number of times to attack (temp)
    while len(enemy_char[HEALTH]) > NO_HEALTH:
        my_char_hearts = ''.join(my_char[1])
        enemy_char_hearts = ''.join(enemy_char[1])
        # Tells the user the round number and the health of each character
        print("\u0332".join("Round {}".format(round)))
        print("""------------------------------------------------------
You({}): \t\t Health: {}
{}: \t\t Health: {}
------------------------------------------------------\n"""
              .format(my_char[NAME], my_char_hearts,
                      enemy_char[NAME], enemy_char_hearts))

        # Calls on user attack functions, then decreases health accordingly
        round_time, user_damage, regen, hp_gained = attacking_user(
            my_char, MOVES, VALID_INPUT, NAME)
        if regen is True:
            my_char = character_health(user_damage, my_char,
                                       regen, HEALTH, hp_gained)
        else:
            enemy_char = character_health(user_damage, enemy_char,
                                          regen, HEALTH, hp_gained)
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
            enemy_beaten = True
            break
        print()

        # Calls on enemy attack functions, then decreases health accordingly
        enemy_damage, regen, hp_gained = attacking_bot(
            enemy_char, MOVES, VALID_INPUT, NAME)
        my_char = character_health(enemy_damage, my_char,
                                   regen, HEALTH, hp_gained)

        # Sets win to false to tell user that they lost
        if len(my_char[HEALTH]) <= NO_HEALTH:
            win = False
            break
        print()
        round += 1
    return total_round_time, round, win, enemy_beaten


def character_health(damage, char, regen, HEALTH, hp_gained):
    """
    Determines characters new health after dmg or healing
    """
    # Modifies health to damage dealt
    if regen is False:
        while damage > 0:
            try:
                char[HEALTH].pop()
                damage -= 1
            except:
                break
    # Modifies health to hearts healed
    elif regen is True:
        while hp_gained > 0:
            try:
                char[HEALTH].append("❤")
                hp_gained -= 1
            except:
                break

    return char


def attacking_user(my_char, MOVES, VALID_INPUT, NAME):
    """
    Attacking function for user
    """
    # Setting vars and constants to be used in attack
    choice = 0
    hp_gained = 0
    ACTION_NAME = 0
    DMG = 1
    regen = False
    # Starts the timer for the round
    # and displays user the moveset for choice
    round_start = time.perf_counter()
    print("What move would you like to do?")
    for number, action in sorted(MOVES.items()):
        if action[ACTION_NAME] != "Dental Visit/Toro Niho\t\t":
            print("({}) to {}\t|\t{} Hearts"
                  .format(number, action[ACTION_NAME], action[DMG]))
        else:
            print("({}) to {}\t|\t+{} Hearts"
                  .format(number, action[ACTION_NAME], action[DMG]))
    print("")
    # Asks user which move they want to do with error check
    # and aknowledges user selection
    while not(choice in VALID_INPUT):
        choice = force_number(("What would you like to do? {}: "
                               .format(VALID_INPUT)))
        if choice in VALID_INPUT:
            break
        print("Please enter a number between 1 and 4\n")
    print("You selected {}!"
          .format((MOVES[choice])[ACTION_NAME].strip()))

    # Timer countdown until trivia will start, gives user time to prepare
    # countdown(3)
    print()

    # Start timer for the trivia begins it
    attack_start = time.perf_counter()
    for number, action in MOVES.items():
        if choice == number:
            if action[ACTION_NAME] != "Dental Visit/Toro Niho\t\t":
                attack = trivia(choice)
                base_damage = action[DMG]
                timer_end = time.perf_counter()
                attack_time = timer_end - attack_start

                # 5% randomised miss rate and randomised crit
                attack = randomised_miss(attack)
                damage, crit = randomised_crit(base_damage)
                # Function that returns damage based on attack and time
                damage = attack_dmg(attack, attack_time,
                                    my_char, damage,
                                    crit, NAME,
                                    (action[ACTION_NAME]).strip())
            else:
                timer_end = time.perf_counter()
                damage = 0
                regen = True
                hp_gained = action[DMG]
                print("{} visited the dentist, and gained {} Hearts!"
                      .format(my_char[NAME], hp_gained))

    # End timer after attack is finished
    # and calcs attack time and round time
    round_time = timer_end - round_start

    return round_time, damage, regen, hp_gained


def attacking_bot(enemy_char, MOVES, VALID_INPUT, NAME):
    """
    Bot that will attack for the enemy
    """
    # Predetermined vars for enemy attack
    base_damage = 3
    attack = True
    regen = False
    hp_gained = 0
    MOVE = "attack"
    # Randomised miss, critcial and attack time for bot
    attack = randomised_miss(attack)
    damage, crit = randomised_crit(base_damage)
    attack_time = random.uniform(0, 6)

    # Lets user know the enemy is attacking and "thinking"
    print("The enemy is attacking...")
    time.sleep(1.5)

    damage = attack_dmg(attack, attack_time, enemy_char,
                        damage, crit, NAME, MOVE)
    return damage, regen, hp_gained


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
    question_sets = [["What is the optimal time to brush teeth for?: ",
                      ["1 Minute", False], ["30 Seconds", False],
                      ["2 Minutes", True],
                      ["1 and a half Minutes", False]],
                     ["How often should you brush your teeth?: ",
                      ["Twice a day", True], ["Once a day", False],
                      ["Every 2 days", False], ["Three times a day", False]],
                     # Mouthwash Q
                     ["What is the optimal time to rinse with mouthwash?: ",
                      ["1 Minute", False], ["30 Seconds", True],
                      ["2 Minutes", False], ["1 and a half Minutes", False]],
                     ["How should you use mouthwash?: ",
                      ["Light Swish", False],
                      ["Light Gargle", False],
                      ["Swish Vigorously and Gargle", True],
                      ["Swish Vigorously", False]],
                     # Floss Q
                     ["What is the optimal length to floss with?: ",
                      ["10cm", False],
                      ["25cm", False], ["60cm", False],
                      ["45cm", True]],
                     ["How often should you floss your teeth?: ",
                      ["Twice a day", False], ["Once a day", True],
                      ["Every 2 days", False],
                      ["Three times a day", False]]]

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
    # Setting empty list to turn into string
    # that will be printed for prompt
    questions = []
    # Copy 4 answers to shuffle, then remakes
    # the question set with shuffled ans
    shuffle_set = question_set[1:]
    random.shuffle(shuffle_set)
    question_set[1:] = shuffle_set

    # Iterates through keys to create the answer matched with key
    # i.e 1: 2 minutes
    for i in range(len(KEYS)):
        question = ("{}: {}".format(KEYS[i], (question_set[i+1])[0]))
        if (question_set[i+1])[1] is True:
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
    q_set = random.randint(0, 1)
    question = questions[q_set]
    # Asks user for ans and then checks if valid
    while not(answer in KEYS):
        answer = force_number("{}\nAnswer Here: "
                              .format(question.prompt))
        if answer in KEYS:
            break
        print("Please enter a number betweeen 1 and 4\n")
    if answer == question.answer:
        attack = True
    else:
        attack = False
    return attack


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


def randomised_crit(base_damage):
    """
    Randomises if damage will be a crit
    """
    crit = False
    hit_rate = random.randint(1, 20)
    crit_number = random.randint(1, 20)
    if hit_rate == crit_number:
        damage = base_damage * 1.5
        crit = True
    else:
        damage = base_damage
    return damage, crit


def attack_dmg(attack, attack_time, character, damage, crit, NAME, move):
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
        damage = int(damage)
        if crit is True:
            print("{} took {:.02f}s to {},"
                  " and dealt a critical hit of {} Hearts!"
                  .format(character[NAME], attack_time, move, damage))
        else:
            print("{} took {:.02f}s to {},"
                  " and dealt {} Hearts!"
                  .format(character[NAME], attack_time, move, damage))
    elif (attack == VALID_ATTACK and attack_time <= MEDIUM and
          attack_time > QUICK):
        damage = int(damage * MED_MULTI)
        if crit is True:
            print("{} took {:.02f}s to {},"
                  " and dealt a critical hit of {} Hearts!"
                  .format(character[NAME], attack_time, move, damage))
        else:
            print("{} took {:.02f}s to {},"
                  " and dealt {} Hearts!"
                  .format(character[NAME], attack_time, move, damage))
    elif attack == VALID_ATTACK and attack_time > MEDIUM:
        damage = int(damage * SLOW_MULTI)
        if crit is True:
            print("{} took {:.02f}s to {},"
                  " and dealt a critical hit of {} Hearts!"
                  .format(character[NAME], attack_time, move, damage))
        else:
            print("{} took {:.02f}s to {},"
                  " and dealt {} Hearts!"
                  .format(character[NAME], attack_time, move, damage))
    else:
        print("{0} did not {1}, {0} missed!"
              .format(character[NAME], move))
        damage = 0

    return damage


def main():
    """
    Welcomes users and calls the turn function to begin the
    RPG based attacks
    """
    # Setting variables and constants
    total_round_time = 0
    VALID_INPUT, MOVES = moves()
    NAME = 0
    HEALTH = 1
    MAX_CHARS = 35
    start = False

    # Welcoming the user and providing context to understand the game
    print("Kia Ora koutou katoa, Welcome to the dental RPG!\n"
          "This game is all about learning dental hygiene!\n"
          "You will be faced against 3 dental enemies and if you"
          " choose the right dental practices you can beat them!\n"
          "If you beat all 3 you win and become a"
          " certified dental champion!\n")
    print("You will be timed on how long it took"
          " you to beat the game and to answer the questions!\n"
          "So try your hardest to be quick!!!\n")
    print("""------------------------------------------
MOVE/NEKE BUFFS:
Move below 2s: 100% move effectiveness
Move inbetween 2-5s: 80% move effectiveness
Move over 5s: 50% move effectiveness
------------------------------------------""")

    username = input("\nWhat is your name?"
                     "/Ko wai tou ingoa?: ").title().strip()
    while username == "" or len(username) > MAX_CHARS:
        print("Please enter a name!/Tomo koa he ingoa!")
        username = input("What is your name?/Ko wai tou ingoa?: ").title()
    print("Kia Ora {}!".format(username))
    print()
    choice = menu("Start the Game/Tīmatahia te Kēmu")

    # Error check and loop to ensure user is ready to start,
    # check highscore or quit
    while choice != 3:
        if choice == 1:
            enemies_beaten = 0
            total_time = 0
            total_rounds = 0
            # Calling characters to get name, and setting users initial health
            my_char, enemy_chars = characters(username, NAME, HEALTH)
            my_char_intial_health = my_char[HEALTH]
            print()

            # Loop through so user will fight all 3 enemies
            while start != "":
                start = input("Press enter to start: ")
            for enemy_char in enemy_chars:
                countdown(1, "Next round starts in: ")
                total_round_time, round, win, enemy_beaten = turn(
                    my_char, my_char_intial_health, enemy_char,
                    total_round_time, MOVES, VALID_INPUT, NAME, HEALTH)

                # Calcs total rounds and time taken(speedrunning purposes)
                total_rounds += round
                total_time += total_round_time
                if enemy_beaten is True:
                    enemies_beaten += 1

                # If statements telling user whether they won or lost
                # With info of total rounds and time taken
                if win is False:
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
                    print("You lost! You took a total of {:.02f}s"
                          " and lasted {} rounds!"
                          .format(total_time, total_rounds))
                    history_write(username, win, enemies_beaten, total_time)
                    break

            if win is True:
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
                print("You took a total of {:.02f}s"
                      " and beat the game in {} rounds!"
                      .format(total_time, total_rounds))

            choice = menu("Replay/Whakahou")
        elif choice == 2:
            history_print()
            print()
            choice = menu("Start the Game/Tīmatahia te Kēmu")

    print("Goodbye...")



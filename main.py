
import random
import time

correctly_guessed_letters = []
incorrectly_guessed_letters = []
randomly_chosen_word = ""

lives_left = 6
game_over = False

def choose_random_word():
    global randomly_chosen_word
    acceptable_words = [
        "Abruptly",
        "Axiom",
        "Bagpipes",
        "Blizzard",
        "Croquet",
        "Flapjack"
    ]

    random.seed(time.time())
    randomly_chosen_word = random.choice(acceptable_words)
    randomly_chosen_word = randomly_chosen_word.lower()

def draw_word():
    global correctly_guessed_letters
    global randomly_chosen_word

    for i in range(0, len(randomly_chosen_word)):
        letter = randomly_chosen_word[i]
        if letter in correctly_guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

def draw_hangman():
    global lives_left
    if lives_left == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           /")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")

def get_one_valid_letter():
    is_letter_valid = False
    letter = ""
    while is_letter_valid is False:
        letter = input("Enter guess letter: ")
        letter = letter.strip().lower()
        if len(letter) <= 0 or len(letter) > 1:
            print("Letter must be of length 1")
        elif letter.isalpha():
            if letter in correctly_guessed_letters or letter in incorrectly_guessed_letters:
                print("You have already guessed the letter " + letter + ", please try again")
            else:
                is_letter_valid = True
        else:
            print("Letter must be (a-z)")

    return letter

def guess_letter():
    global correctly_guessed_letters
    global incorrectly_guessed_letters
    global lives_left

    letter = get_one_valid_letter()
    if letter in randomly_chosen_word:
        correctly_guessed_letters.append(letter)
    else:
        incorrectly_guessed_letters.append(letter)
        lives_left -= 1






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





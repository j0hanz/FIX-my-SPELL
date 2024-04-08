import word_art
import os
import time
import sys
import random
from words import Words


def text_effect_fast(text):
    for letter in text:
        if letter == "\n":
            print("\n")
        else:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.01)
    print()


def text_effect(text):
    """
    Create typing effect to improve user experience.
    """
    for letter in text:
        if letter == "\n":
            print("\n")
        else:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.06)
    print()


def clear_terminal():
    """
    Clears the terminal.
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system("cls" if os.name == "nt" else "clear")


def user_input():
    """
    Function to request a user's name and return it.
    """
    user_name = ""
    while True:
        text_effect("What is your name?")
        text_effect_fast("Press enter If you dont want to disclose your name")
        user_name = input("").capitalize()
        if user_name == "":
            user_name = "User"
            break
        elif not user_name.isalpha():
            clear_terminal()
            print("(ᴗ˳ᴗ)".ljust(400))
            text_effect(f"{user_name}?\nIs that really your name?")
            text_effect("Nah try again.\n")
        else:
            break
    return user_name


def game_rules(data):

    if data == "Y":
        print(word_art.instructions)
        text_effect("Press enter to continue")
        input("")
        clear_terminal()
        return True
    elif data == "N":
        return True

    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")


def choose_word(used_words):
    """
    Randomly selects a word from the list that hasn't been used yet
    """
    available_words = [word for word in Words if word not in used_words]
    if not available_words:
        print("End")
        return random.choice(Words)
    return random.choice(available_words)


def scramble_word(word):
    """
    Scrambles the letters of the word, keeping the first and last letters unchanged
    """
    first_letter = word[0]
    last_letter = word[-1]
    middle_letters = list(word[1:-1])
    random.shuffle(middle_letters)
    return first_letter + "".join(middle_letters) + last_letter


def start_game():
    print(word_art.game)
    used_words = []
    words_to_play = 10
    for _ in range(words_to_play):
        # Choose a word that hasn't been used yet and scramble it
        word = choose_word(used_words)
        if word is None:
            break
        used_words.append(word)
        scrambled_word = scramble_word(word)

        print(scrambled_word.ljust(400))
        text_effect("Enter your guess: ")
        guess = input("").lower()

        if guess == word:
            print("Good job!.")
            time.sleep(2)
            clear_terminal()
            print(word_art.game)
        else:
            print("Nope...", word)
            time.sleep(2)
            clear_terminal()
            print(word_art.game)


def play_again():
    while True:
        text_effect("Do you want to restart the game?")
        restart = input("(Y/N): ").upper()
        if restart == "Y":
            return True
        if restart == "N":
            clear_terminal()
            thank_you_message()
            main()
            return False
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.\n")


def thank_you_message():
    text_effect("Thanks for playing!")
    time.sleep(1)
    text_effect_fast("Heading back to start menu...")
    time.sleep(2)
    clear_terminal()


def welcome_message():
    print(word_art.welcome)
    text_effect("WELCOME TO FIX-my-SPELL!")
    time.sleep(1)
    text_effect_fast("Starting in...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    clear_terminal()


def main():
    welcome_message()
    print(word_art.welcome)
    user_name = user_input()
    clear_terminal()
    print(word_art.welcome)
    print("⊂(◉‿◉)つ".ljust(400))
    text_effect(f"Hello {user_name}!\n")
    time.sleep(1)
    while True:
        text_effect("Do you want to read the rules?")
        rules_input = input("(Y/N): ").upper()
        clear_terminal()
        if game_rules(rules_input):
            break

    while True:
        text_effect(f"Press enter to start the game {user_name}!  (✪‿✪) ")
        input("")
        text_effect_fast("Starting in...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        break
    clear_terminal()
    start_game()

    if play_again():
        clear_terminal()
        start_game()


main()

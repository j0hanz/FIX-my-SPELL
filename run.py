import word_art
import os
import time
import sys
from stages import spell_stages


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
    Credit: https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system("cls" if os.name == "nt" else "clear")


def game_rules(data):

    if data == "Y":
        print(word_art.instructions)
        input("Press any key")
        clear_terminal()
        return True
    elif data == "N":
        return True

    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")


def start_game():
    print(word_art.game)


def play_again():
    while True:
        text_effect("Do you want to restart the game?")
        restart = input("(Y/N): ").upper()
        if restart == "Y":
            return True
        if restart == "N":
            clear_terminal()
            main()
            return False
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.\n")


def main():
    print(word_art.welcome)
    print("Hello! ⊂(◉‿◉)つ".ljust(200))

    while True:
        name = input("Enter your name please: ").capitalize()
        if not name.isalpha():
            print(f"Is that your name? Nah try again.\n")
        else:
            break

    clear_terminal()

    text_effect(f"Hello {name}!\nWelcome to FIX-my-SPELL!")
    while True:
        text_effect("Do you want to read the rules?")
        rules_input = input("(Y/N): ").upper()
        clear_terminal()
        if game_rules(rules_input):
            break

    while True:
        text_effect("Press any key to start the game!  (✪‿✪) ")
        input("")

        break
    clear_terminal()
    start_game()

    if play_again():
        clear_terminal()
        start_game()


main()

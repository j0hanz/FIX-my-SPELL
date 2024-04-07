import word_art
import os
from stages import spell_stages


def clear_terminal():
    """
    Clears the terminal.
    """
    # From:
    # https://stackoverflow.com/questions/2084508/clear-terminal-in-python

    os.system("cls" if os.name == "nt" else "clear")


def game_rules(data):

    if data == "Y":
        print(word_art.instructions)
        return True

    elif data == "N":
        return True

    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")


def start_game():
    print(word_art.game)


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

    print(f"Hello {name}! Welcome to FIX-my-SPELL!".ljust(200))
    while True:
        rules_input = input("Do you want to read the rules? (Y/N): ").upper()
        if game_rules(rules_input):
            break

    while True:
        level_input = input("Press any key to start the game!  (✪‿✪) ")

        break
    clear_terminal()
    start_game()


main()

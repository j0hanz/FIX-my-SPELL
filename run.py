from colorama import Fore
import word_art
import os
import time
import sys
import random
from words import Words


"""

Constant Varibles

"""
MAX_ATTEMPTS = 3
WORDS_TO_PLAY = 10
DISPLAY_CURRENT_WORD = 1


class color:
    """

    Function that makes (active_word) from word_art BOLD

    """

    BOLD = "\033[2m"
    END = "\033[0m"


def remove_line():
    """

    Move cursor to the beginning of the line

    """
    sys.stdout.write("\033[F")


def text_effect_fast(text):
    """

    Create typing effect to improve user experience.

    """
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
    Targets messages.

    """
    for letter in text:
        if letter == "\n":
            print("\n")
        else:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.03)
    print()


def get_valid_answer():
    """

    This function validates If user enters a letter.
    If user didn't type a letter, It will stay and ask for valid answer.

    """
    while True:
        user_input = input("-> ")
        remove_line()

        if user_input.isalpha():
            return user_input.lower()
        print(Fore.RED + "Invalid choice!" + Fore.RESET, "You can only use letters:")


def game_over_victory():
    """

    When user finished the game, this function will run.

    """
    clear_terminal()
    print(Fore.GREEN + word_art.victory.ljust(200) + Fore.RESET)
    print(Fore.GREEN + "ヾ(＾∇＾)".ljust(200) + Fore.RESET)
    text_effect("Well done! You completed the game!")
    time.sleep(3)
    text_effect_fast("Press 'Enter' to exit the game.")
    input("")
    text_effect_fast("Leaving...")
    time.sleep(1)
    clear_terminal()
    play_again()


def game_over_fail():
    """

    When user has run out of attempts, this function will run.

    """
    clear_terminal()
    print(Fore.RED + word_art.lose.ljust(200) + Fore.RESET)
    print(Fore.RED + "(눈_눈)".ljust(200) + Fore.RESET)
    text_effect("All attempts are used, you lost the game...")
    time.sleep(3)
    text_effect_fast("Press 'Enter' to move on.")
    input("")
    text_effect_fast("heading back...")
    time.sleep(1)
    clear_terminal()
    play_again()


def clear_terminal():
    """

    Clears the terminal.
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python

    """
    os.system("cls" if os.name == "nt" else "clear")


def user_input():
    """

    Function that requests a user's name and returns it.

    """
    user_name = ""
    while True:
        text_effect("What is your name?")
        time.sleep(0.5)
        text_effect_fast("Press enter If you dont want to disclose your name")
        user_name = input("").capitalize()
        if user_name == "":
            user_name = "User"
            break
        elif not user_name.isalpha():
            clear_terminal()
            print("".ljust(200))
            print(Fore.YELLOW + "(ᴗ˳ᴗ)" + Fore.RESET)
            text_effect(f"{user_name}?\nIs that really your name?")
            text_effect("Nah try again.\n")
        else:
            break
    return user_name


def game_rules(data):
    """

    Data for how to play. User can choose to show the rules for the game.
    Or continue without showing the rules.

    """
    if data == "Y":
        print(word_art.instructions)
        text_effect("Press enter to continue")
        input("")
        clear_terminal()
        return True
    elif data == "N":
        return True

    else:
        print(Fore.BLUE + word_art.welcome + Fore.RESET)
        print("Invalid choice. Please enter 'Y' or 'N'.")


def choose_word(used_words):
    """

    Randomly selects a word from the list that hasn't been used yet.
    All words are located in 'words.py' file.

    """
    available_words = [word for word in Words if word not in used_words]
    if not available_words:
        print("End")
        return random.choice(Words)
    return random.choice(available_words)


def scramble_word(word):
    """

    Scrambles the letters of the word, here I have decided to keep the first and last letters unchanged.

    """
    first_letter = word[0]
    last_letter = word[-1]
    middle_letters = list(word[1:-1])
    random.shuffle(middle_letters)
    return first_letter + "".join(middle_letters) + last_letter


def display_wrong_answer(display_current, attempts, scrambled_word, word):
    """

    When User answered correct, this function will run.

    """

    print(Fore.RED + word_art.wrong + Fore.RESET)
    print(
        Fore.GREEN + f"| {display_current}/10 |" + Fore.RESET,
        Fore.RED + f"     | {attempts} 💔  |" + Fore.RESET,
    )
    print(Fore.RED + color.BOLD + word_art.active_word + color.END + Fore.RESET)
    print(
        Fore.RED + scrambled_word + Fore.RESET,
        "     [ The right word was:",
        Fore.YELLOW + word + Fore.RESET,
        "]",
    )
    print(Fore.RED + color.BOLD + word_art.active_word + color.END + Fore.RESET)
    print(Fore.RED + "(눈_눈)".ljust(200) + Fore.RESET)
    print("Wrong...".ljust(200))
    time.sleep(1)
    text_effect_fast("Moving on...")
    time.sleep(3)
    clear_terminal()


def display_right_answer(display_current, attempts, scrambled_word):
    """

    When User answered wrong, this function will run.
    Also shows the correct word.

    """

    print(Fore.GREEN + word_art.right + Fore.RESET)
    print(
        Fore.GREEN + f"| {display_current}/10 |" + Fore.RESET,
        Fore.RED + f"     | {attempts} 💚  |" + Fore.RESET,
    )
    print(Fore.GREEN + color.BOLD + word_art.active_word + color.END + Fore.RESET)
    print(Fore.GREEN + scrambled_word + Fore.RESET)
    print(Fore.GREEN + color.BOLD + word_art.active_word + color.END + Fore.RESET)
    print(Fore.GREEN + "⊂(◉‿◉)つ".ljust(200) + Fore.RESET)
    print("Correct!.".ljust(200))
    time.sleep(1)
    text_effect_fast("Moving on...")
    time.sleep(3)
    clear_terminal()


def start_game():
    """

    Function that starts the game.

    """
    used_words = []
    words_to_play = WORDS_TO_PLAY
    attempts = MAX_ATTEMPTS
    display_current = DISPLAY_CURRENT_WORD
    for _ in range(words_to_play):
        """

        Choose a word that hasn't been used yet and scramble it

        """
        word = choose_word(used_words)

        if display_current == 10:
            game_over_victory()

        if attempts == 0:
            game_over_fail()

        if word is None:
            break

        used_words.append(word)
        scrambled_word = scramble_word(word)
        print(word_art.game)
        print(
            Fore.GREEN + f"| {display_current}/10 |" + Fore.RESET,
            Fore.RED + f"     | {attempts} 🤍  |" + Fore.RESET,
        )
        print(color.BOLD + word_art.active_word + color.END)
        print(scrambled_word)
        print(color.BOLD + word_art.active_word + color.END)
        print("".ljust(200))
        guess = get_valid_answer()
        clear_terminal()

        if guess == word:

            display_right_answer(display_current, attempts, scrambled_word)

        else:

            display_wrong_answer(display_current, attempts, scrambled_word, word)
            attempts -= 1

        display_current += 1


def play_again():
    """

    When the game Is finished, the game will ask If User wants to play again.

    """
    clear_terminal()
    print(Fore.BLUE + word_art.welcome + Fore.RESET)
    text_effect("Do you want to restart the game?")
    while True:
        restart = input("(Y/N): ").upper()
        if restart == "Y":
            text_effect_fast("Great! Restarting the game...")
            time.sleep(2)
            clear_terminal()
            start_game()
            return True

        elif restart == "N":
            clear_terminal()
            thank_you_message()
            main()
            return False
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.\n")


def thank_you_message():
    """

    If user doesn't want to continue playing,
    A thank you message will appear and heads back to start screen.

    """
    print(Fore.BLUE + word_art.welcome + Fore.RESET)
    text_effect("Thanks for playing!")
    time.sleep(1)
    text_effect_fast("Heading back to start menu...")
    time.sleep(2)
    clear_terminal()


def welcome_message():
    """

    Function that welcomes users to the game,
    this Is the first function that will appear on the screen.

    """
    print(Fore.BLUE + word_art.welcome + Fore.RESET)
    text_effect_fast("Starting in...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    clear_terminal()


def main():
    """

    Main function

    """
    welcome_message()
    print(Fore.BLUE + word_art.welcome + Fore.RESET)
    user_name = user_input()
    clear_terminal()
    print(Fore.BLUE + word_art.welcome + Fore.RESET)
    print(Fore.YELLOW + "⊂(◉‿◉)つ".ljust(200) + Fore.RESET)
    text_effect(f"Hello {user_name}!\n")
    time.sleep(1)
    while True:
        text_effect_fast("Do you want to read the rules?")
        rules_input = input("(Y/N): ").upper()
        clear_terminal()
        if game_rules(rules_input):
            break

    while True:
        print(Fore.BLUE + word_art.welcome + Fore.RESET)
        print(Fore.YELLOW + "(✪‿✪)" + Fore.RESET.ljust(200))
        text_effect(f"Press enter to start the game {user_name}!")
        input("")
        text_effect_fast("Starting in...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        clear_terminal()
        start_game()
        break

    if play_again():
        clear_terminal()
        start_game()


main()

from colorama import Fore
import word_art
import os
import time
import sys
import random
from words import Words


class color:
    """

    Function that makes (line) from word_art BOLD

    """

    BOLD = "\033[2m"
    END = "\033[0m"


"""

Constant Varibles

"""
MAX_ATTEMPTS = 3
WORDS_TO_PLAY = 11
DISPLAY_CURRENT_WORD = 1
RED_LINE = Fore.RED + color.BOLD + word_art.line + color.END + Fore.RESET
GREEN_LINE = Fore.GREEN + color.BOLD + word_art.line + color.END + Fore.RESET
BOLD_LINE = color.BOLD + word_art.line + color.END
LOGO = Fore.BLUE + word_art.welcome + Fore.RESET
GAME = word_art.game
GAME_WRONG_ANSWER = Fore.RED + word_art.game + Fore.RESET
GAME_CORRECT_ANSWER = Fore.GREEN + word_art.game + Fore.RESET
GAME_VICTORY = Fore.GREEN + word_art.victory.ljust(200) + Fore.RESET
GAME_FAIL = Fore.RED + word_art.lose.ljust(200) + Fore.RESET
RULES = word_art.instructions
SAD_SMILE = Fore.RED + "(눈_눈)".ljust(200) + Fore.RESET
CONFUSED_FACE = Fore.YELLOW + "(・・)" + Fore.RESET
ANGRY_FACE = Fore.RED + "(⩺_⩹)".ljust(200)
HAPPY_FACE = Fore.GREEN + "⊂(◉‿◉)つ".ljust(200) + Fore.RESET


def start_count():
    text_effect_fast("Starting in...")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)


def remove_line():
    """

    Clears the current line in the console.
    https://stackoverflow.com/questions/36520120/overwriting-clearing-previous-console-line

    """
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


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

    Create typing effect to improve user experience,
    slower writing compare to the above function.

    """
    for letter in text:
        if letter == "\n":
            print("\n")
        else:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.03)
    print()


def rules_answer():
    """
    Validates the user's input for yes or no.
    """
    while True:
        valid_input = input("(Y/N) -> ").upper()
        remove_line()
        if valid_input == "Y":
            clear_terminal()
            print(RULES)
            text_effect("Press enter to continue")
            input("")
            clear_terminal()
            return True
        elif valid_input == "N":
            return True
        else:
            try:
                # If user typed a number.
                if valid_input.isnumeric():
                    raise ValueError(
                        f"[ {valid_input} ] \nI didn't ask for a number.")
                # If user didn't entered a letter.
                if not valid_input.isalpha():
                    raise ValueError(
                        f"[ {valid_input} ] \nThat's not what i asked.")
                # If user only entered more than one letter.
                if len(valid_input) >= 2:
                    raise ValueError(
                        f"[ {valid_input} ] \nYou can only enter one letter."
                    )
                # If user entered a letter but not Y or N.
                if valid_input.isalpha():
                    raise ValueError(
                        f"[ {valid_input} ] \nPlease enter 'Y' or 'N'.")
            except ValueError as e:
                print(Fore.RED + "Invalid choice:" +
                      Fore.RESET, f"{e} Try again...\n")
                remove_line()


def get_valid_answer():
    """

    This function validates If user enters a letter.
    If user didn't type a letter, It will stay and ask for a valid answer.
    Also If user accidentally typed one letter, the answer will be invalid.

    """
    while True:
        user_input = input("-> ")
        remove_line()
        # Minimum of 2 letters to accept an answer.
        if user_input.isalpha() and len(user_input) >= 2:
            return user_input.lower()
        else:
            try:
                # If user typed a number.
                if user_input.isnumeric():
                    raise ValueError(f"{user_input} \nThere is no number...")
                # If user didn't entered a letter.
                if not user_input.isalpha():
                    raise ValueError(
                        f"{user_input} \nOnly letters are allowed...")
                # If user only entered one letter.
                if user_input.isalpha():
                    raise ValueError(
                        f"{user_input} \nYou only wrote one letter...")
            except ValueError as e:
                print(
                    Fore.RED + "Invalid answer!" + Fore.RESET,
                    f"{e}",
                )


def game_over_victory():
    """

    When user finished the game, this function will run.

    """
    clear_terminal()
    print(GAME_VICTORY)
    print(Fore.GREEN + "ヾ(＾∇＾)".ljust(200) + Fore.RESET)
    text_effect("Well done! You completed the game!")
    time.sleep(3)
    text_effect_fast("Press 'Enter' to exit the game.")
    input("")
    text_effect_fast("Leaving...")
    sys.stdout.write("\033[F")
    time.sleep(1)
    clear_terminal()
    play_again()


def game_over_fail():
    """

    When user has run out of attempts, this function will run.

    """
    clear_terminal()
    print(GAME_FAIL)
    print(SAD_SMILE)
    text_effect("All attempts are used... Game over!")
    time.sleep(2)
    text_effect_fast("Leaving...")
    sys.stdout.write("\033[F")
    time.sleep(2)
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
        user_name = input("-> ").capitalize()
        if user_name == "":
            user_name = "User"
            break
        elif not user_name.isalpha():
            clear_terminal()
            print(LOGO)
            print(CONFUSED_FACE)
            text_effect(f"{user_name}?\nIs that really your name?")
            text_effect("Nah try again.\n")
        else:
            break
    return user_name


def choose_word(used_words):
    """

    Randomly selects a word from the list that hasn't been used yet.
    All words are located in 'words.py' file.

    """
    available_words = [word for word in Words if word not in used_words]
    return random.choice(available_words)


def scramble_word(word):
    """

    Scrambles the letters of the word, here I have decided to keep the first,
    second and last letters unchanged.

    """
    first_letter = word[0]
    second_letter = word[1]
    last_letter = word[-1]
    middle_letters = list(word[2:-1])
    random.shuffle(middle_letters)
    return first_letter + second_letter + "".join(middle_letters) + last_letter


def display_wrong_answer(display_current, attempts, scrambled_word,
                         word, guess):
    """

    When User answered wrong, this function will run.
    Also shows the correct word.

    """

    print(GAME_WRONG_ANSWER)
    print(f"| {display_current}/10 |" f"     | {attempts} 💔  |")
    print(RED_LINE)
    print(
        Fore.RED + scrambled_word,
        "     WRONG!" + Fore.RESET,
        "The right word was: (",
        Fore.YELLOW + word + Fore.RESET,
        ")",
    )
    print(RED_LINE)
    print(ANGRY_FACE)
    print("You answerd:" + Fore.RESET, Fore.YELLOW + guess + Fore.RESET)
    time.sleep(2)
    text_effect_fast("Moving on...")
    sys.stdout.write("\033[F")
    time.sleep(3)
    clear_terminal()


def display_right_answer(display_current, attempts, scrambled_word, guess):
    """

    When User answered correct, this function will run.

    """

    print(GAME_CORRECT_ANSWER)
    print(f"| {display_current}/10 |" f"     | {attempts} 💚  |")
    print(GREEN_LINE)
    print(Fore.GREEN + scrambled_word, "      CORRECT!" + Fore.RESET)
    print(GREEN_LINE)
    print(HAPPY_FACE)
    print(Fore.GREEN + "You answerd:" + Fore.RESET,
          Fore.YELLOW + guess + Fore.RESET)
    time.sleep(1)
    text_effect_fast("Moving on...")
    sys.stdout.write("\033[F")
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

        if display_current == words_to_play:
            game_over_victory()

        if attempts == 0:
            game_over_fail()

        if word is None:
            break

        used_words.append(word)
        scrambled_word = scramble_word(word)
        print(word_art.game)
        print(f"| {display_current}/10 |" f"     | {attempts} 🤍  |")
        print(BOLD_LINE)
        print(scrambled_word)
        print(BOLD_LINE)
        print("".ljust(200))
        guess = get_valid_answer()
        clear_terminal()

        if guess == word:

            display_right_answer(display_current, attempts,
                                 scrambled_word, guess)

        else:

            display_wrong_answer(display_current, attempts,
                                 scrambled_word, word, guess)
            attempts -= 1

        display_current += 1


def play_again():
    """

    When the game Is finished, the game will ask If user wants to play again.

    """
    clear_terminal()
    print(LOGO)
    text_effect("Do you want to restart the game?")
    while True:
        restart = input("(Y/N) -> ").upper()
        if restart == "Y":
            clear_terminal()
            print(LOGO)
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
            try:
                # If user typed a number.
                if restart.isnumeric():
                    raise ValueError(
                        f"[ {restart} ] \nI didn't ask for a number.")
                # If user didn't entered a letter.
                if not restart.isalpha():
                    raise ValueError(
                        f"[ {restart} ] \nThat's not what i asked.")
                # If user only entered more than one letter.
                if len(restart) >= 2:
                    raise ValueError(
                        f"[ {restart} ] \nYou can only enter one letter."
                    )
                # If user entered a letter but not Y or N.
                if restart.isalpha():
                    raise ValueError(
                        f"[ {restart} ] \nPlease enter 'Y' or 'N'.")
            except ValueError as e:
                print(Fore.RED + "Invalid choice:" +
                      Fore.RESET, f"{e} Try again...\n")
                remove_line()


def thank_you_message():
    """

    If user doesn't want to continue playing,
    A thank you message will appear and heads back to start screen.

    """
    print(LOGO)
    text_effect("Thanks for playing!")
    time.sleep(1)
    text_effect_fast("Leaving...")
    sys.stdout.write("\033[F")
    time.sleep(2)
    clear_terminal()


def start_screen():
    """

    First screen that will appear when starting the game

    """
    while True:
        start_count()
        break
    clear_terminal()


def main():
    """

    Main function

    """
    start_screen()
    print(LOGO)
    user_name = user_input()
    clear_terminal()
    print(LOGO)
    print(HAPPY_FACE)
    text_effect(f"Hello {user_name}!\n")
    time.sleep(1)
    while True:
        text_effect_fast("Do you want to read the rules?")
        if rules_answer():
            clear_terminal()
            break

    while True:
        print(LOGO)
        print(Fore.GREEN + "(✪‿✪)" + Fore.RESET.ljust(200))
        text_effect(f"Let's get started {user_name}!")
        time.sleep(1)
        start_count()
        break
    clear_terminal()
    start_game()

    if play_again():
        clear_terminal()
        start_game()


'''

This ensures that main() is only called when the script is executed directly.


'''
if __name__ == "__main__":

    main()

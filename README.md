
![logo](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/a848ebda-e872-4e95-a57c-865cf2cba7e3)

#### [Play here!](https://fix-my-spell-7e3aef96045e.herokuapp.com/)


# Contents :mag_right:

- [FIX-my-SPELL Game](#fix-my-spell-game)
  - [User Stories](#user-stories)
    - [User Goals](#user-goals)
  - [User Experience](#user-experience)
- [Features](#features)
  - [Future Implementations](future-implementations)
- [How to play](#how-to-play)
- [Technologies used](#technologies-used)
- [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
  - [Bugs](#bugs)
    - [Known Issues](#known-issues)
    - [Fixed bugs](#fixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

# FIX-my-SPELL Game

Fix My Spell is a Python console-based game where players are tasked with correcting misspelled words. It presents players with words containing intentional spelling errors, and their objective is to identify and rectify these errors to form the correct word. The game is targeted towards individuals of all ages who are interested in enhancing their vocabulary and spelling skills in a fun and interactive way.

## User Stories

xxxxxx

### User Goals

xxxxxx

## User Experience

* Intuitive Interface: The game interface is designed to be straightforward and easy to navigate.

* Clear Instructions: The [How to Play](#how-to-play) section provides instructions to understand the game mechanics.

* Optional Features: Optional elements such as reading the game rules before playing.

* Feedback Mechanisms: The game provides feedback to players for their actions, such as notifying them of correct or incorrect answers.

* Gameplay: With words containing intentional spelling errors, players are challenged to think, figure out the word and how it is spelled.

* Replayability: Upon completing the game or failed, players have the option to restart.

# Features

* Randomly selects words from a predefined list and scrambles them for the player to unscramble.

* Provides a limited number of attempts for each word.

* Displays game status, including current word, remaining attempts, and progress.

* Gives feedback on correct and incorrect answers.

* Supports replayability with an option to restart the game.

#### Progress

![progress_bar](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/86d3b5b5-7942-42b4-ba5d-ac1ef19a5f52)

__________________________________________________________________________________________________________

#### Attempts

![numer_of_attempts](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/ae7d0b0f-bade-49a0-944d-7ceb30257ae3)

__________________________________________________________________________________________________________

#### Current Word

![current_word](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/f029caf1-3768-4e76-ad1f-ccfe7c7dc5c3)

__________________________________________________________________________________________________________

#### Type you guess here

The arrow icon shown below is where you type

![type_here](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/9dace81d-361c-4f62-8898-f5295d4f2afc)

__________________________________________________________________________________________________________

![restart_game](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/5334c59f-f4bb-42ef-ad3d-323a767fdb3d)

__________________________________________________________________________________________________________


## Future Implementations

### Difficulty Levels

* Introduce multiple difficulty levels (e.g., Easy, Medium, Hard) to cater to players of varying skill levels.
* Adjust parameters such as the number of attempts allowed per word, the complexity of the words, and the time limit for each round based on the selected difficulty level.

### Word Categories

* Implement a feature that allows players to select different word categories (e.g., Animals, Food, Sports) to diversify the gameplay experience.

# How to play

Playing Fix My Spell is simple and straightforward. Follow these steps to enjoy the game:

1. Start the Game: Execute the main Python script to launch the game interface in the console. Live version here [->](https://fix-my-spell-7e3aef96045e.herokuapp.com/)

   ![start_screen](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/4dfe3f62-d6a8-46e3-a34c-a7d7cbb7fe91)

   __________________________________________________________________________________________________________


2. Enter Your Name (Optional): When prompted, provide your name for personalized interactions within the game. If user leaves it empty, the game will give you a name as 'User'.

   ![user_name_request](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/f9d0c9b1-28c9-445f-8368-435234571d21)

   __________________________________________________________________________________________________________

5. Read the Rules (Optional): Decide whether you want to read the game rules. Respond with "Y" for Yes or "N" for No.
   word_wrong

#### Displays if user left their name empty

  ![read_rules_y_n](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/57ecff0b-d092-4036-93ef-33b981c49ebb)

  __________________________________________________________________________________________________________

#### Displays if user entered a name

  ![read_rules_name_enterd](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/4ce491bb-fea2-4c27-86d0-a06d4c03e9bc)

  __________________________________________________________________________________________________________

7. Begin Correcting Words: Once the game starts, you will be presented with words containing intentional spelling errors. Your task is to identify and correct these errors to form the correct word.

  ![display_word](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/07687553-92d7-4b2e-a232-25d81f906c18)

  __________________________________________________________________________________________________________

9. Input Your Answer: Enter your corrected version of the word when prompted. Ensure that your input consists of alphabetical characters and is at least two characters in length.

#### Correct answer

  ![word_correct](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/5e7b7036-7c89-4c55-b414-2dfebc4c0443)

  __________________________________________________________________________________________________________

#### Wrong answer

  ![word_wrong](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/cf1488a7-526a-4997-86b3-8aebe5a62497)
  __________________________________________________________________________________________________________

11. Continue Playing: Repeat steps 4 and 5 for each word presented by the game. Be mindful of the number of attempts available for each word.

12. Victory or Defeat: Complete all words successfully to achieve victory, or exhaust your attempts to experience defeat. You can choose to play again or exit the game once it concludes.

#### Victory

  ![victory](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/92181512-1a50-49e3-bdc1-72ae4767032c)

  __________________________________________________________________________________________________________

#### Fail

  ![game_over](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/fa0710f7-a65f-40c5-9bd9-158e81d312e3)

  __________________________________________________________________________________________________________

14. Enjoy and Learn: Have fun while enhancing your vocabulary and spelling skills in an engaging and interactive gaming experience!

# Technologies used

* Python: The core programming language used to develop the game logic and functionality.

* Colorama: A Python library utilized for adding colored text and styling to the console output, enhancing the visual appeal of the game.

* Word Art: Another Python library employed for generating ASCII art text, contributing to the visual presentation of the game interface.

# Testing

### Manual testing

I have extensively tested the code numerous times, both locally in the terminal and on the deployed site Heroku using the mock terminal.
I gave the game wrong or weird information to see how it reacts.

### Automated testing

I used Code Institutes own validator [CI Python Linter](https://pep8ci.herokuapp.com/).

#### run.py

![code_check](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/044b76f4-7d55-420a-8591-2ad0ec0f39a8)

#### word_art.py & words.py file

Similar tests were conducted on these files as well. While words.py showed no errors, 
word_art.py presented several issues, including:

* invalid escape sequence

* trailing whitespace

* blank line contains whitespace

These errors stem from text generated via a third-party application, [Fancy Text Generator](https://www.fancytextpro.com/)

The affected file only contains text displayed on top.

#### Example image:

![word_art](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/25c2e33d-8d9e-4375-a4a6-18e142f77282)

## Bugs

xxxxxx

### Known Issues

xxxxxx

### Fixed bugs

xxxxxx

# Deployment

xxxxxx

# Credits
xxxxxx

### Code

xxxxxx

### Acknowledgements

xxxxxx


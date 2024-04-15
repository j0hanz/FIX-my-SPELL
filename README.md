
![logo](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/a848ebda-e872-4e95-a57c-865cf2cba7e3)

### Practise and challenge your spelling knowledge! :heavy_check_mark:

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
    - [Heroku](#heroku)
    - [Github](#github)
- [Credits](#credits)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

# FIX-my-SPELL Game

Fix My Spell is a Python console-based game where players are tasked with correcting misspelled words. It presents players with words containing intentional spelling errors, and their objective is to identify and rectify these errors to form the correct word. The game is targeted towards individuals of all ages who are interested in enhancing their vocabulary and spelling skills in a fun and interactive way.

## Flowchart

#### Preview

This is the first drawing for this game. Done via [Lucidchart](https://www.lucidchart.com/pages/)

![FIX-my_SPELL_PP3](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/64074b1d-ff79-4c46-a219-ce5f501b18d3)


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

## Existing Features

Word Scramble Gameplay:
* Randomly selects words from a predefined list and scrambles them for the player to unscramble.

Interactive User Interface:
* Engage with a colorful and dynamic console interface, featuring ASCII art and colorful text.

Typing Effects:
* Experience smooth and immersive typing effects for a more interactive user experience.

Handling User Input:
* If the user enters a value that is not requested, a error message will display.
* Example:
  - Numeric Input
  - Non-Alphabetic Characters
  - Single Letter Input (When guessing a word)

__________________________________________________________________________________________________________

### Example imgages:

![Invalid_YES](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/eea66c1f-1068-47fc-a84a-f9e1ca469095)

__________________________________________________________________________________________________________

![Invalid_word+!](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/1af99837-717a-4a10-a625-e704fa0adb0f)

__________________________________________________________________________________________________________

![Invalid_T](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/46fc14b7-6c5c-4b59-b6e3-34334246017c)

__________________________________________________________________________________________________________

![Invalid_number](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/542fc786-fdea-4aba-af1b-4125e540c711)

__________________________________________________________________________________________________________

![Invalid_guess_number](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/e8d06b70-81e1-418b-b7d1-9e348bb87a22)

__________________________________________________________________________________________________________

![Invalid_Enter](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/6f1958f6-c3d6-41b7-a76b-6f3f0c9f9254)

__________________________________________________________________________________________________________

Limited Attempts:
* Provides a limited number of attempts for each wrong answer.

![numer_of_attempts](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/ae7d0b0f-bade-49a0-944d-7ceb30257ae3)

__________________________________________________________________________________________________________

Play Again:
* Supports replayability with an option to restart the game.

![restart_game](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/5334c59f-f4bb-42ef-ad3d-323a767fdb3d)

__________________________________________________________________________________________________________

#### Progress

![progress_bar](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/86d3b5b5-7942-42b4-ba5d-ac1ef19a5f52)

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

* [Python](https://www.python.org/downloads/): The core programming language used to develop the game logic and functionality.

* [Colorama](https://pypi.org/project/colorama/): A Python library utilized for adding colored text and styling to the console output, enhancing the visual appeal of the game.
* [Fancy Text Generator](https://www.fancytextpro.com/) - 
* [Github](https://github.com/) - To save and store files for this site.
* [Heroku](https://www.heroku.com/) - Used to deploy the live project
* [Gitpod](https://www.gitpod.io/) - For workspace.
* [Spell Checker](https://chromewebstore.google.com/detail/spell-checker-for-chrome/jfpdnkkdgghlpdgldicfgnnnkhdfhocg) - For spell control.
* [Reverso](https://www.reverso.net/spell-checker/english-spelling-grammar/) - For spell & grammar control.

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

The app was deployed through Heroku. The steps are as following:

Login (or signup) to [Heroku](https://id.heroku.com/login) and [Github](https://github.com/login)

### Heroku

1. After creating a Heroku account, click "New" to create a new app from the dashboard.

2. Enter a unique app name, select your region and click "Create app".

3. Navigate to settings tab and scroll down to view the Config Vars section and click "Reveal Config Vars".

4. Enter port into the Key box and 8000 into the Value box and click the Add button.

5. Navigate to Buildpacks and click "Add buildpack".

6. First add Python, then add NodeJS into Buildpacks. (Ensure that it is in order!)

![heroku](https://github.com/j0hanz/FIX-my-SPELL/assets/159924955/3a387388-680e-45cb-bcc2-1571903264d1)

7. Navigate to Deply tab (same navigationbar as settings).

8. Choose GitHub as the Deployment method.

9. Search for the repository name, select the branch that you would like to build from, and connect it via the "Connect" button.

10. Choose from "Automatic" or "Manual" deployment options, I went for automatic. Click "Deploy Branch".

11. When the build is finished, click "View" link to bring you to your deployed site. You can also find the link via Settings -> Domains.
__________________________________________________________________________________________________________

### Github

Go to the repository for this project -> [FIX-my-SPELL](https://github.com/j0hanz/FIX-my-SPELL/tree/main)

#### Forking

Click the Fork button in the top right corner.

#### Clone

1. Click the button called Code

2. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.

3. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.

4. Type 'git clone' into the terminal and then paste the link you copied. Press enter.

__________________________________________________________________________________________________________

# Credits
xxxxxx

### Code

xxxxxx

### Acknowledgements

xxxxxx


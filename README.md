# **BATTLESHIP PY**

![Live Project Mockup](/assets/images/battleship-responsive.png)

[Link to Live Project](https://battleship-py-2024-04ee4b5ff686.herokuapp.com/)

## Table of Contents

- [**BATTLESHIP PY**](#battleship-py)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [UX](#ux)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
  - [Testing](#testing)
  - [Errors](#errors)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Cloning the GitHub Repository](#cloning-the-github-repository)
  - [Credits](#credits)

## Introduction

Battleship Py is a CLI (Command-Line Interface) game that can be run with little processor power. The player battles against the computer in a classic strategic war game made famous by Hasbro as a board game classic. Like the board game, the player has the ability to strategically place 5 ships (The ships are: Aircraft Carrier (5), Battleship (4), Submarine (3),Destroyer (3), and Patrol Boat (2)) on the 10 X 10 game grid. The player's opponent is the computer. The computer randomly places the same number and type of ships on it's own 10 X 10 grid. The ship placement on the computer's 10 X 10 grid (board) is hidden from the player and vice versa. The player has a choice of placing the ships either vertically or horizontally between coordinate parameters A-J and 1-8. Constant scoring updates and feedback updates the player throughout the game until the player has either won or lost. the first player (or computer as the opponent) to sink all 5 of the opponent's ships has won the game.

## UX

### User Stories

| ID | As a... | I Want To Be Able To... | So That I Can... |

| --- | ---------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

| 01 | Game Enthusiast | a simple strategy game | Simple instructions at beginning of game. I have the ability to strategically place my ships as I can with the board game. Game also gives me constant score updates and feedback on invalid coordinates, as well as if I have won or lost. |

| 02 | Older middle-aged vintage computers enthusiast | Classic CLI game for nostalgia. | I can relive my childhood by running a good old fashioned command line game.Easy to run and can play whilst doing other tasks on my computer. |

| 03 | Young student learning python | I can play games like my parents did back in the day and have fun studying at school. | I can run this on single board computer projects for school and hobby.

Main Menu in Development:

![Main Menu](/assets/images/main-menu.png)

Main Menu Choices:

![Main Menu](/assets/images/menu-choices-1.png)

User message x:

![Message x](/assets/images/user-message-x.png)

User message y:

![Message y](/assets/images/user-message-y.png)

Game Play with the player has won message:

![Game play](/assets/images/battleship-player-won.png)

Updated Start Screen:

![Updated Start Screen](/assets/images/battleship-start-screen.png)

Computer has won message:

![Computer has won message](/assets/images/computer-won.png)

|

### Wireframes

- No wireframes were required for this project.

## Features

- Command-line Interface "vintage style" game easily run with little processor power and other resources from the computer, thus the ability to run on older computers.

- Player has the added strategic ability of playing the ships, just like the original board game.

- Clear instructions as to how to play the game.

- Consistent score updates and game feedback to the player with every strategic move.

### Existing Features

*Intro welcome message with instructions.

![Welcome message](/assets/images/battleship-menu.png)

![10 X 10 game grid](/assets/images/game-grids.png)

### Features Left to Implement

- Describe some features that we would like to implement in the future

- Add additional colors to the game through Colorama included with python and some additional ASCII art.

- Expand on the game play messages to expand the game.

- Use a Python Game Engine such as Ursina Engine for a complete 2D GUI experience.

- Eventually develop further as an Android app.

## Technologies Used

- [VS Code](https://en.wikipedia.org/wiki/Visual_Studio_Code)

Code Editor

![VSCode](/assets/images/vscodelogo.png)

- [GitHub](https://github.com/)

Code Repository

![GitHub](/assets/images/github.png)

- [git](https://www.git-scm.com/)

Version Control

![git](/assets/images/git.png)

- [Heroku](https://en.wikipedia.org/wiki/Heroku)

Deployment

![Heroku](/assets/images/herokulogo.png)

- [Taskade](https://www.taskade.com/)

AI Tool

![Taskade](/assets/images/taskade.png)

### Languages Used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

![Python](/assets/images/python-logo-only.png)

## Testing

- [Ruff](https://docs.astral.sh/ruff/)

used as a Formatter and Linter for the Python Code

![Ruff](/assets/images/ruff.png)

- [pre-commit](https://pre-commit.com/)

used to correct any formatting or linting errors prior to pushing the code to GitHub

![pre-commit](/assets/images/precommit.png)

- [CI Python Linter](https://pep8ci.herokuapp.com/)

used for Python Code validation

![CI Python Linter](/assets/images/ci.png)

## Errors

A debugging error was noticed during the VS Code debugging session. The CI Python Linter was able to assist in fixing this error:

![Debug Error](/assets/images/debug-error.png)

There were issues with the game logic, starting with how the ships were checked for hits and misses. Every time the Computer played a move, the coordinates chosen was indicated as a hit, even when it should have been a miss.

Taskade AI assisted me in solving this issue:

Taskade Response:

"The issue seems to be in the part where the computer moves and checks for hits and misses. Specifically, the condition for checking hits and misses may not be correctly identifying the ships on the player's board.

Let's revise the computer's move logic to ensure it correctly identifies and registers hits and misses.

Key Points to Check and Adjust

Identify Ships Correctly: The condition to check if a shot is a hit or miss should correctly identify ship parts by checking for characters other than consts.CHAR_WATER or already marked consts.CHAR_HIT and consts.CHAR_MISS.

Formatting Cells: Ensure that the ship cells are correctly identified in their original format (without Fore and Style formatting).

Let's update the logic accordingly."

Explanation:

Check for Ships Correctly:

"Updated the condition to check if the cell contents are part of the ship, i.e., player_board y x should not be any of the empty or already hit/miss cells: not in [consts.CHAR_WATER, consts.CHAR_HIT, consts.CHAR_MISS]."

After updating the code, the ships were checked correctly to indicate a hit or a miss.

Another issue was duplicate ships were generating on the game boards of both the computer and and player. Using the Python shell, I was able to identify the issue and correct it, confirming with the Python shell output:

![Ship Placement Python Shell output](/assets/images/correct-board-placement.png)

Confirmed corrected game logic in development:

![Corrected game play](/assets/images/updated-game-logic.png)

## Deployment

### Heroku

This program was deployed to Heroku, following the below steps:

Push most up-to-date code to Github

Create a list of requirements by typing the following into the terminal: pip3 freeze > requirements.txt

Push the requirements to Github

Logon to Heroku

Select create new app

Add app name

Add app region

Select 'Create app'

Open up the Settings tab, on the top ribbon

In 'Config Vars' select 'Reveal Config Vars'

Add 'PORT' as a key and '8000' as a value

In 'Buildpacks' select 'Add buildpack' and choose python. Then, repeat for nodejs (order is important; python first followed by nodejs)

Navigate to 'Deploy' on the top ribbon

In 'Deployment method', select 'Github', once clicked it should say 'connected'

Enter a repository in Github to connect to and click 'Search'

Once repository has been found, click 'Connect' to link new app to Github repository

In 'Automatic deploys', select the 'Enable Automatic Deploy' option

To view your command line on the Heroku platform, once a new code has been pushed to Github, log on to Heroku

Select the required app that appears on your home screen

Select 'Open app' on the right hand side of the screen

The app should appear in a new tab on the web browser

The link to my Heroku app is: <https://cli-battleship-game.herokuapp.com/>

### Forking the GitHub Repository

The following steps can be used to fork the GitHub repository:

- On GitHub navigate to the main page of the repository.

- The 'Fork' button can be found on the top right-hand side of the screen.

- Click the button to create a copy of the original repository.

### Cloning the GitHub Repository

The following steps can be used to clone the GitHub repository:

- On GitHub navigate to the main page of the repository.

- Above the list of files select 'Code'.

- Three options are provided, HTTPS, SSH and GitHub CLI. Select the appropriate option and click the 'Copy' button next to the URL.

- Open Git Bash.

- Change the working directory to the location for the cloned directory.

- Type git clone and paste the copied URL.

- Press 'Enter' to create the clone.

## Credits

- My Mentor at Code Institute : Martina

- [Code Institute](https://codeinstitute.net/)

- MY Python coach [Bob Belderbos](https://github.com/bbelderbos)

- Senior Data Engineer [Bob Belderbos](https://github.com/bbelderbos)

- [Pybites Circle Community](https://pybites.circle.so/)

- [Pybites](https://pybit.es/)

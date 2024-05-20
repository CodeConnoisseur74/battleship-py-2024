# **BATTLESHIP PY**

![Live Project Mockup](https://ui.dev/amiresponsive?url=https://battleship-py-2024.herokuapp.com/)

[Link to Live Project](https://battleship-py.herokuapp.com/)

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
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Cloning the GitHub Repository](#cloning-the-github-repository)
  - [Credits](#credits)
    - [Code](#code)

## Introduction

Battleship Py is a CLI (Command-Line Interface) game that can be run with little processor power. The player battles against the computer in a classic strategic war game made famous by Hasbro as a board game classic. Like the board game, the player has the ability to strategically place the ships on the 10 X 10 game grid. The player has a choice of placing the ships either vertically or horizonntally between coordinate parameters A-J and 1-8. Constant scoring updates and feedback updates the player throughout the game until the player has either won or lost.

## UX

### User Stories

| ID  | As a...                                        | I Want To Be Able To...                                                               | So That I Can...                                                                                                                                                                                                                           |
| --- | ---------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 01  | Game Enthusiast                                | a simple strategy game                                                                | Simple instructions at beginning of game. I have the ability to strategically place my ships as I can with the board game. Game also gives me contant score updates and feedback on invalid coordinates, as well as if I have won or lost. |
| 02  | Older middle-aged vintage computers enthusiast | Classic CLI game for nostalgia.                                                       | I can relive my childhood by running a good old fashioined commandline game.Easy to run and can play whilst doing other tasks on my computer.                                                                                              |
| 03  | Young student learning python                  | I can play games like my parents did back in the day and have fun studying at school. | I can run this on single board computer projects for school and hobby.                                                                                                                                                                     |

### Wireframes

- No wireframes were required for this project.

## Features

*Command-line Interface "vintage style" game easily run with little processor power and other resources from the computer, thus the ability to run on older computers.
*Player has the added strategic ability of playing the ships, just like the original board game.
*Clear instructions as to how to play the game.
*Consistent score updates and game feedback to the player with every strategic move.

### Existing Features

*Intro welcome message with instructions.

![Welcome message](/images/project3intro.png)

![10 X 10 game grid](/images/project3gameplay.png)

### Features Left to Implement

- Describe some features that we would like to implement in the future

*Add color to the game through Colorama included with python and some ASCII art.

*Expand on the gameplay messages to expand the game.

*Use GamePy for a complete 2D GUI expereince.

*Eventually devolp further as an Android app.

## Technologies Used

### Languages Used

*[Python](https://en.wikipedia.org/wiki/Python_(programming_language))

![Python](/images/python-logo-only.png)

*[VS Code](https://en.wikipedia.org/wiki/Visual_Studio_Code)

![VSCode](/images/vscodelogo.png)

*[Pycharm](https://en.wikipedia.org/wiki/JetBrainse)

![VSCode](/images/PyCharmlogo.png)

*[Heroku](https://en.wikipedia.org/wiki/Heroku)

![Heroku](/images/herokulogo.png)

### Frameworks, Libraries & Programs Used

*[Random](https://docs.python.org/3/library/random.html)

## Testing

PEP8, Pylint and Black Formatter was used to test and find errors. Only syntax errors were found. Renaming of functions and variables according to PEP8 documentation was carried out and refactored using PyCharm before confirming and copying over to VSCode in Gitpod.

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

    The link to my Heroku app is: https://cli-battleship-game.herokuapp.com/

### Forking the GitHub Repository

The following steps can be used to fork the GitHub repository:

- On GitHub navigate to the main page of the repository.
- The 'Fork' button can be found on the top righthand side of the screen.
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

### Code

- Credit and articles etc that we have copied code from

*[PEP8](https://peps.python.org/pep-0008/)

*[Al Sweigart, Author of Python Text Books for No Startch Press](https://alsweigart.com/)

- Any other credits

<https://github.com/Stephanie-Ash/suburban-walking/blob/master/README.md>

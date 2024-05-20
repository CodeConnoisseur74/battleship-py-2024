# import sys
# import random
# from colorama import Fore, Style, init
# import string
import types

# Constants
consts = types.SimpleNamespace()
consts.CHAR_HIT = "X"
consts.CHAR_WATER = "."
consts.CHAR_MISS = "-"
consts.BOARD_SIZE = 10
consts.SHIP_TYPES = {
    "Aircraft Carrier": 5,
    "Battleship": 4,
    "Submarine": 3,
    "Destroyer": 3,
    "Patrol Boat": 2,
}


# Function to convert alphabetic y-coordinate to numeric coordinate
def convert_alphabetic_to_numeric(letter: str):
    return ord(letter.upper()) - ord("A")


# Function to convert numeric y-coordinate to alphabetic coordinate
def convert_numeric_to_alphabetic(numeric: int):
    return chr(ord("A") + numeric)

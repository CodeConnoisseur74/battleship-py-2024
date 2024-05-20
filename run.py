# import sys
# import random
from colorama import Fore, Style, init

# import string
import types

# Initialize colorama
init()

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


def format_cell(cell: str, show_ships) -> str:
    match cell:
        case consts.CHAR_HIT:
            return Fore.RED + cell + Style.RESET_ALL
        case consts.CHAR_MISS:
            return Fore.WHITE + cell + Style.RESET_ALL
        case consts.CHAR_WATER:
            return Fore.CYAN + cell + Style.RESET_ALL
        case _:
            return (
                Fore.YELLOW + cell + Style.RESET_ALL
                if show_ships
                else Fore.CYAN + consts.CHAR_WATER + Style.RESET_ALL
            )


# Function to initialize an empty game board
def initialize_board():
    board = []
    for _ in range(consts.BOARD_SIZE):
        row = [consts.CHAR_WATER] * consts.BOARD_SIZE
        board.append(row)
    return board

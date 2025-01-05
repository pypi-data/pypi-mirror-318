"""Setup game settings and constants"""

import json
import os
import pygame as pg
from math import sqrt

pg.init()
useless_screen = pg.display.set_mode()

FONT = pg.font.SysFont("Calibri", 42)

# Directories
FILE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(FILE_DIR, "images")
AI_DIR = os.path.join(FILE_DIR, "ai_files")

# Colours
BACKGROUND = (30, 30, 30)
DEAD_ZONE = (141, 141, 141)
WHITE = (255, 255, 255)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
BLUE2 = (158, 190, 228, 255)
RED = (255, 0, 0)
RED2 = (207, 46, 46)
YELLOW = (255, 255, 0)
YELLOW2 = (249, 217, 84, 255)
GREEN = (0, 255, 0)
GREEN2 = (39, 151, 0)
GREEN3 = (102, 203, 112)
ARROW_COLOR = (255, 0, 247)

# Images (free to use)
# https://www.iconshock.com/flat-icons/3d-graphics-icons/sphere-icon/
MARBLE_RED = pg.image.load(
    os.path.join(IMAGES_DIR, "marble_red.png")
    ).convert_alpha()
MARBLE_GREEN = pg.image.load(
    os.path.join(IMAGES_DIR, "marble_green.png")
    ).convert_alpha()
MARBLE_PURPLE = pg.image.load(
    os.path.join(IMAGES_DIR, "marble_purple.png")
    ).convert_alpha()
MARBLE_BLUE = pg.image.load(
    os.path.join(IMAGES_DIR, "marble_blue.png")
    ).convert_alpha()
MARBLE_YELLOW = pg.image.load(
    os.path.join(IMAGES_DIR, "marble_yellow.png")
    ).convert_alpha()
MARBLE_FREE = pg.image.load(
    os.path.join(IMAGES_DIR, "marble_empty.png")
    ).convert_alpha()
# https://icons8.com/icon/54885/skull
SKULL = pg.image.load(
    os.path.join(IMAGES_DIR, "skull.png")
).convert_alpha()
SKULL = pg.transform.rotozoom(SKULL, 0, 0.7)  # Adjusting size
# Dead marbles
DEAD_BLUE = MARBLE_BLUE.copy()
DEAD_BLUE.blit(SKULL, (8, 8))
DEAD_YELLOW = MARBLE_YELLOW.copy()
DEAD_YELLOW.blit(SKULL, (8, 8))

MARBLE_SIZE = MARBLE_RED.get_rect().size[0]  # All marbles have the same size
MAX_DISTANCE_MARBLE = MARBLE_SIZE*sqrt(1.25) # Max distance between two neighbouring marbles (diagonal)


# Window size
WIDTH = 900
FIRST_X = WIDTH*0.6 - MARBLE_SIZE*2.5
FIRST_Y = 65  # Defines window's height
HEIGHT = FIRST_Y*2 + MARBLE_SIZE*9

# Keys are arbitrary chosen
MARBLE_IMGS = {
    -2: DEAD_BLUE,
    -3: DEAD_YELLOW,
    1: MARBLE_FREE,
    2: MARBLE_BLUE,
    3: MARBLE_YELLOW,
}

# Texts
# Current Player Blue
CURRENT_PLAYERB_TXT = "Playing: Blue"
CURRENT_PLAYERB_FONT_SIZE = 35
CURRENT_PLAYERB_COLOR = BLUE2
CURRENT_PLAYERB_POSITION = WIDTH*0.01, FIRST_Y*0.15
CURRENT_PLAYERB = [
    CURRENT_PLAYERB_TXT,
    CURRENT_PLAYERB_FONT_SIZE,
    CURRENT_PLAYERB_COLOR,
    CURRENT_PLAYERB_POSITION
]
# Current Player Yellow
CURRENT_PLAYERY_TXT = "Playing: Yellow"
CURRENT_PLAYERY_FONT_SIZE = CURRENT_PLAYERB_FONT_SIZE
CURRENT_PLAYERY_COLOR = YELLOW2
CURRENT_PLAYERY_POSITION = WIDTH*0.01, FIRST_Y*0.15
CURRENT_PLAYERY = [
    CURRENT_PLAYERY_TXT,
    CURRENT_PLAYERY_FONT_SIZE,
    CURRENT_PLAYERY_COLOR,
    CURRENT_PLAYERY_POSITION
]
# Blue wins
BLUE_WINS_TXT = "Blue wins! Reset or quit?"
BLUE_WINS_FONT_SIZE = 35
BLUE_WINS_COLOR = BLUE2
BLUE_WINS_POSITION = WIDTH*0.01, FIRST_Y*0.15
BLUE_WINS = [
    BLUE_WINS_TXT,
    BLUE_WINS_FONT_SIZE,
    BLUE_WINS_COLOR,
    BLUE_WINS_POSITION
]
# Yellow wins
YELLOW_WINS_TXT = "Yellow wins! Reset or quit?"
YELLOW_WINS_FONT_SIZE = 35
YELLOW_WINS_COLOR = YELLOW2
YELLOW_WINS_POSITION = WIDTH*0.01, FIRST_Y*0.15
YELLOW_WINS = [
    YELLOW_WINS_TXT,
    YELLOW_WINS_FONT_SIZE,
    YELLOW_WINS_COLOR,
    YELLOW_WINS_POSITION 
]
# draw
DRAW_TXT = "The game is drawn! Reser or quit?"
DRAW_FONT_SIZE = 35
DRAW_COLOR = GREY
DRAW_POSITION = WIDTH*0.01, FIRST_Y*0.15
DRAW = [
        DRAW_TXT,
        DRAW_FONT_SIZE,
        DRAW_COLOR,
        DRAW_POSITION
]
# Confirm move
CONFIRM_MOVE_TXT = "Spacebar to move"
CONFIRM_MOVE_FONT_SIZE = 35
CONFIRM_MOVE_COLOR = GREEN2
CONFIRM_MOVE_POSITION = WIDTH*0.01, FIRST_Y*0.7
CONFIRM_MOVE = [
    CONFIRM_MOVE_TXT,
    CONFIRM_MOVE_FONT_SIZE,
    CONFIRM_MOVE_COLOR,
    CONFIRM_MOVE_POSITION
]
# Wrong move
WRONG_MOVE_TXT = "Invalid move"
WRONG_MOVE_FONT_SIZE = 35
WRONG_MOVE_COLOR = RED2
WRONG_MOVE_POSITION = CONFIRM_MOVE_POSITION
WRONG_MOVE = [
    WRONG_MOVE_TXT,
    WRONG_MOVE_FONT_SIZE,
    WRONG_MOVE_COLOR,
    WRONG_MOVE_POSITION
]
# Reset Game
RESET_GAME_TXT = "Reset Game [r]"
RESET_GAME_FONT_SIZE = 30
RESET_GAME_COLOR = GREY
RESET_GAME_POSITION = WIDTH*0.01, FIRST_Y*9.25
RESET_GAME = [
    RESET_GAME_TXT,
    RESET_GAME_FONT_SIZE,
    RESET_GAME_COLOR,
    RESET_GAME_POSITION
]
# Quit Game
QUIT_GAME_TXT = "Quit Game [q]"
QUIT_GAME_FONT_SIZE = 30
QUIT_GAME_COLOR = GREY
QUIT_GAME_POSITION = WIDTH*0.01, FIRST_Y*9.75
QUIT_GAME = [
    QUIT_GAME_TXT,
    QUIT_GAME_FONT_SIZE,
    QUIT_GAME_COLOR,
    QUIT_GAME_POSITION
]

# Deadzones
# Position
FIRST_DZ_X = 70
FIRST_BDZ_Y = FIRST_Y + MARBLE_SIZE
FIRST_YDZ_Y = FIRST_Y + MARBLE_SIZE*5
# Blue
BLUE_DEADZONE = {
    (FIRST_DZ_X, FIRST_BDZ_Y): 1,
    (FIRST_DZ_X + MARBLE_SIZE, FIRST_BDZ_Y): 1,
    (FIRST_DZ_X + MARBLE_SIZE*2, FIRST_BDZ_Y): 1,
    (FIRST_DZ_X + MARBLE_SIZE*0.5, FIRST_BDZ_Y + MARBLE_SIZE): 1,
    (FIRST_DZ_X + MARBLE_SIZE*1.5, FIRST_BDZ_Y + MARBLE_SIZE): 1,
    (FIRST_DZ_X + MARBLE_SIZE, FIRST_BDZ_Y + MARBLE_SIZE*2): 1,
}
# Yellow
YELLOW_DEADZONE = {
    (FIRST_DZ_X + MARBLE_SIZE, FIRST_YDZ_Y): 1,
    (FIRST_DZ_X + MARBLE_SIZE*0.5, FIRST_YDZ_Y + MARBLE_SIZE): 1,
    (FIRST_DZ_X + MARBLE_SIZE*1.5, FIRST_YDZ_Y + MARBLE_SIZE): 1,
    (FIRST_DZ_X, FIRST_YDZ_Y + MARBLE_SIZE*2): 1,
    (FIRST_DZ_X + MARBLE_SIZE, FIRST_YDZ_Y + MARBLE_SIZE*2): 1,
    (FIRST_DZ_X + MARBLE_SIZE*2, FIRST_YDZ_Y + MARBLE_SIZE*2): 1,
}

# Initial Configurations
STANDARD = [
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2],
    [1, 1, 2, 2, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 3, 3, 3, 1, 1],
    [3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
]
GERMAN_DAISY = (
    [1, 1, 1, 1, 1],
    [2, 2, 1, 1, 3, 3],
    [2, 2, 2, 1, 3, 3, 3],
    [1, 2, 2, 1, 1, 3, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 3, 1, 1, 2, 2, 1],
    [3, 3, 3, 1, 2, 2, 2],
    [3, 3, 1, 1, 2, 2],
    [1, 1, 1, 1, 1],
)
BELGIAN_DAISY = (
    [3, 3, 1, 2, 2],
    [3, 3, 3, 2, 2, 2],
    [1, 3, 3, 1, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 1, 3, 3, 1],
    [2, 2, 2, 3, 3, 3],
    [2, 2, 1, 3, 3],
)
DUTCH_DAISY = (
    [2, 2, 1, 3, 3],
    [2, 3, 2, 3, 2, 3],
    [1, 2, 2, 1, 3, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 3, 1, 2, 2, 1],
    [3, 2, 3, 2, 3, 2],
    [3, 3, 1, 2, 2],
)
SWISS_DAISY = (
    [1, 1, 1, 1, 1],
    [2, 2, 1, 1, 3, 3],
    [2, 3, 2, 1, 3, 2, 3],
    [1, 2, 2, 1, 1, 3, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 3, 1, 1, 2, 2, 1],
    [3, 2, 3, 1, 2, 3, 2],
    [3, 3, 1, 1, 2, 2],
    [1, 1, 1, 1, 1],
)
DOMINATION = (
    [1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 3],
    [2, 2, 1, 1, 1, 3, 3],
    [2, 2, 2, 2, 1, 3, 3, 3],
    [1, 1, 1, 3, 1, 3, 1, 1, 1],
    [3, 3, 3, 1, 2, 2, 2, 2],
    [3, 3, 1, 1, 1, 2, 2],
    [3, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1],
)
PYRAMID = (
    [2, 1, 1, 1, 1],
    [2, 2, 1, 1, 1, 1],
    [2, 2, 2, 1, 1, 1, 1],
    [2, 2, 2, 2, 1, 1, 1, 1],
    [2, 2, 2, 2, 1, 3, 3, 3, 3],
    [1, 1, 1, 1, 3, 3, 3, 3],
    [1, 1, 1, 1, 3, 3, 3],
    [1, 1, 1, 1, 3, 3],
    [1, 1, 1, 1, 3],
)
THE_WALL = (
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 1],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [1, 3, 3, 3, 3, 3, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 3, 1, 1],
)

CONFIGURATIONS = {
    "standard": STANDARD,
    "classic": STANDARD,
    "belgiandaisy": BELGIAN_DAISY,
    "germandaisy": GERMAN_DAISY,
    "dutchdaisy": DUTCH_DAISY,
    "swissdaisy": SWISS_DAISY,
    "domination": DOMINATION,
    "pyramid": PYRAMID,
    "thewall": THE_WALL,
    "wall": THE_WALL
    }

# ai settings
PLAYER_TYPE = "type"
HUMAN = "human"
AI = "ai"
P_TYPES = {HUMAN, AI}

AI_WEIGHTS = os.path.join(AI_DIR, "mz-weights.h5")

MOVE_IDS = {}
with open(os.path.join(AI_DIR, r"moves2idx-red-permutated.json"),
          "r", encoding="utf-8") as file:
    MOVE_IDS = json.load(file)

MCTS_NUMBER = "mcts_number"
MCTS_NUMBER_DEFAULT = 250

MCTS_DEPTH = "mcts_depth"
MCTS_DEPTH_DEFAULT = 13

PROB_SUM = "prob_sum"
PROB_SUM_DEFAULT = 0.95

DEFAULT_PLAYER = {
    PLAYER_TYPE: HUMAN,
    MCTS_NUMBER: MCTS_NUMBER_DEFAULT,
    MCTS_DEPTH: MCTS_DEPTH_DEFAULT,
    PROB_SUM: PROB_SUM_DEFAULT
    }

PG2AI = {
    1: 0,
    2: 2,
    3: 1
}

AI2PG = {
    0: 1,
    1: 3,
    2: 2,
    }

# error message
ARGV_HELP = """usage game_ai.py:
python game_ai.py [-h] [-s <settings.json>] [-b <position>]
                  [--blue <player-type>] [--blue_mcts <integer>]
                  [--blue_depth <integer>] [--blue_probsum <integer>]
                  [--yellow <player-type>] [--yellow_mcts <integer>]
                  [--yellow_depth <integer>] [--yellow_probsum <integer>]

optinional arguments:
    -h, --help          show this help message and exit
    -s <settings.json>, --settings  <settings.json>
                        .json-file containing the game setup. If provided,
                        options will be primarily taken from that file. All
                        settings not provided within the file, will be set to
                        the other, given arguement values (or their default
                        value if they were not specified at all)
    -b <position>, --board <position>
                        chooses starting positions, available positions are:
                          classic / standard, belgian_daisy, german_daisy,
                          dutch_daisy, swiss_daisy, domination, pyramid,
                          wall / the_wall
                        (default: belgian_daisy)
                        Note:
                          The A.I. was mainly trained on the 'Beglian Daisy'
                          position, so it might play much worse on the other
                          starting positions
    --blue <player-type>
                        sets the player for the blue marbles to human or A.I.,
                        available options are: human, ai (default: human)
    --blue_mcts <integer>
                        sets the number of simulations for the Monte-Carlo tree
                        searches performed at every move for the blue player 
                        (if it is an A.I). This drastically influences playing
                        strength of the A.I, but also the time it needs to
                        calculate for a move (default: 250)
    --blue_depth <integer>
                        sets the depth of the MCTS search for the blue player
                        (if it is an A.I). For every search the number of
                        'blue_depth' moves will be performed and the position
                        evaluated afterwards
                        (default: 13)
    --blue_probsum <float>
                        For the root of the MCTS tree only the moves with the
                        highest probabilities summing up to 'blue_probsum' will
                        be considered. For all later nodes this restriction is
                        not in place
                        (default: 0.95)
    --yellow <player-type>
                        sets the player for the yellow marbles to human or A.I.,
                        available options are: human, ai (default: ai)
    --yellow_mcts integer>
                        sets the number of simulations for the Monte-Carlo tree
                        searches performed at every move for the blue player 
                        (if it is an A.I). This drastically influences playing
                        strength of the A.I, but also the time it needs to
                        calculate for a move (default: 250)
    --yellow_depth <integer>
                        sets the depth of the MCTS search for the yellow player
                        if it is an A.I). For every search the number of
                        'yewllow_depth' moves will be performed and the
                        position evaluated afterwards
                        (default: 13)
    --yellow_probsum <float>
                        For the root of the MCTS tree only the moves with the
                        highest probabilities summing up to 'yewllow_probsum'
                        will be considered. For all later nodes this
                        restriction is not in place
                        (default: 0.95)
"""

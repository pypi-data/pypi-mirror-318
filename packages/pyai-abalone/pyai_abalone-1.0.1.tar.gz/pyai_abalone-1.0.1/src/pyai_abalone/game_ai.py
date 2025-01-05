import sys
import getopt
import re
import json

from os import listdir

import pyai_abalone.constants as const
from pyai_abalone import GameAI


# Game loop
def main(argv):
    conf, player_blue, player_yellow = script_argv(argv)
    board = GameAI(conf, player_blue, player_yellow)
    board.start_game()


def script_argv(argv):
    position = const.BELGIAN_DAISY
    player_blue = {
        const.PLAYER_TYPE: const.HUMAN,
        const.MCTS_NUMBER: const.MCTS_NUMBER_DEFAULT,
        const.PROB_SUM: const.PROB_SUM_DEFAULT
        }
    player_yellow = {
        const.PLAYER_TYPE: const.AI,
        const.MCTS_NUMBER: const.MCTS_NUMBER_DEFAULT,
        const.PROB_SUM: const.PROB_SUM_DEFAULT
        }

    try:
        opts, args = getopt.getopt(
            argv,"hs:b:",
            ["help", "settings", "board=",
             "blue=", "blue_mcts=", "blue_probsum=",
             "yellow=", "yellow_mcts=", "yellow_probsum="])
    except getopt.GetoptError:
        print(const.ARGV_HELP)
        sys.exit(2)

    settings_file = None
    for opt, arg in opts:
        if opt == '-h':
            print(const.ARGV_HELP)
            sys.exit()
        elif opt in ("-b", "--board"):
            pos_name = re.sub(r"[^a-z]", "", arg.lower())
            position = const.CONFIGURATIONS.get(pos_name)
            if position is None:
                position = const.BELGIAN_DAISY
        elif opt in ("-s", "--settings"):
            settings_file = arg
        elif opt == "blue":
            player_blue[const.PLAYER_TYPE] = check_player_type(arg)
        elif opt == "blue_mcts":
            player_blue[const.MCTS_NUMBER] = check_mcts_num(arg)
        elif opt == "blue_probsum":
            player_blue[const.PROB_SUM] = check_prob_sum(arg)
        elif opt == "yellow":
            player_yellow[const.MODEL_TYPE] = check_model_type(arg)
        elif opt == "yellow_mcts":
            player_yellow[const.MCTS_NUMBER] = check_mcts_num(arg)
        elif opt == "blue_probsum":
            player_yellow[const.PROB_SUM] = check_prob_sum(arg)
    
    if settings_file is not None and settings_file in listdir():
        with open(settings_file, "r", encoding="utf-8") as file:
            settings = json.load(file)

        position = const.CONFIGURATIONS.get(
            re.sub(r"[^a-z]", "",
                   settings.get("position", "belgiandaisy").lower()))
        if position is None:
            position = const.BELGIAN_DAISY

        player_checks = {
            const.PLAYER_TYPE: check_player_type,
            const.MCTS_NUMBER: check_mcts_num,
            const.PROB_SUM: check_prob_sum
            }

        blue = settings.get("player_blue")
        if blue is not None:
            for key in player_yellow:
                player_blue[key] = player_checks.get(
                    key, arg_pass)(blue.get(key, ""))
        
        yellow = settings.get("player_yellow")
        if yellow is not None:
            for key in player_yellow:
                player_yellow[key] = player_checks.get(
                    key, arg_pass)(yellow.get(key, ""))

    return position, player_blue, player_yellow


def check_player_type(arg):
    if arg.lower() in const.P_TYPES:
        return arg.lower()
    return const.HUMAN


def check_model_type(arg):
    if arg.lower() in const.M_TYPES:
        return arg.lower()
    return const.MODEL_SMALL


def check_mcts_num(arg):
    try:
        num = int(arg)
    except ValueError:
        return const.MCTS_DEFAULT
    if num > 0:
        return num
    return const.MCTS_DEFAULT


def check_prob_sum(arg):
    try:
        prob_sum = float(arg)
    except ValueError:
        return const.PROB_SUM_DEFAULT
    if prob_sum < 0.8:
        return const.PROB_SUM_DEFAULT
    elif prob_sum > 1.0:
        return 1.0
    return prob_sum


def arg_pass(arg):
    return arg


if __name__ == "__main__":
    main(sys.argv[1:])
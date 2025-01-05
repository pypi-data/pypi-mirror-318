# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:50:06 2023

@author: hlocke
"""

from colorama import Fore, Style
from collections import defaultdict
from .constants import MOVE_IDS
import numpy as np
from .starting_positions import BELGIAN_DAISY
from typing import Dict, List, Any, Tuple


MOVE_DIRECTIONS = [[1, 0], [1, -1], [0, 1], [-1, 0], [-1, 1], [0, -1]]
MOVE_DIRECTIONS = np.array(MOVE_DIRECTIONS, dtype=np.int16)
MOVE_BROADSIDES = {
    (1, 0): [[1, -1], [0, 1]],
    (1, -1): [[0, 1], [-1, 0]],
    (0, 1): [[-1, 0], [-1, 1]],
    (-1, 0): [[-1, 1], [0, -1]],
    (-1, 1): [[0, -1], [1, 0]],
    (0, -1): [[1, 0], [1, -1]]
    }
for move_dir, move_broadside in MOVE_BROADSIDES.items():
    MOVE_BROADSIDES[move_dir] = np.array(move_broadside, dtype=np.int16)


class NumpyAbalone():
    """
    Abalone implementation for python

    Implementation of the 'Abalone' game for Python using the numpy labrary.
    There exist other implementations as well, but they are rather slow.
    The board is representated by a numpy array. Empty field contain the value
    0, white marbles are represented by 1 and black marbles by 2. To acchieve
    the hexagonal shape some entries consists of 'off-board' fields, value = 3.
    
    Args:
        board: np.ndarray, (defaults to BELGIAN_DAISY), starting position for
            the game
        black_tomove: Boolean (defaults to True). Whether or not black will
            have to make the next move
        move_history: List (defaults to []), stores the reached positions
        move_hist_save: Boolean (defaults to True). Whether or not the store
            the played moves.
        move_counter: collections.defaultdict(int), (defaults to empty 
            defaultdict). Stores how often every position was reached. This is
            used to check repetitions of moves
        turn_number: int, (defaults to 1). number of the current turn
        noloss_turns: int, (defaults to 0). number of turns without a marble
            loss
        noloss_moves: int, (defaults to 0). number of moves without a marble
            loss
    """
    multi_move = 3  # maybee change to variable size in future
    marble_loss_end = 6  # maybee change to variable size in future
    reps_to_draw = 3  # maybee change to variable size in future
    noloss_draw = 50  # maybee change to variable size in future
    marble_max = 14  # standard value
    center_win = 0

    def __init__(self,
                 board: np.ndarray = BELGIAN_DAISY,
                 black_tomove: bool = True,
                 move_history: List[np.ndarray] = [],
                 move_hist_save: bool = True,
                 move_counter: defaultdict(int) = defaultdict(int),
                 turn_number: int = 1,
                 noloss_turns: int = 0,
                 noloss_moves: int = 0):

        self.board = board

        self.black_loss = self.marble_max - np.sum(
            np.where(self.board == 2, 1, 0))
        self.white_loss = self.marble_max - np.sum(
            np.where(self.board == 1, 1, 0))

        # game state in result
        self.move_history = move_history
        self.move_hist_save = move_hist_save
        if self.move_hist_save and len(self.move_history) == 0:
            self.move_history.append(self.board)
        self.move_counter = move_counter
        self.turn_number = turn_number
        self.noloss_turns = noloss_turns
        self.noloss_moves = noloss_moves
        self.black_tomove = black_tomove
        self.game_ended = False
        # -1 = black wins | 0 = draw | 1 = white wins | 10 = game did not end
        self.result = 10

    def get_current_game_stats(self) -> Dict[str, Any]:
        """
        creates a dictionary containing the necessary paramters to initiate a
        copy of this class instance
        
        Returns: dict, containing the parameter to initiate a copy of this
            class instance
        """
        stats = {
            "board": self.board,
            "black_tomove": self.black_tomove,
            "move_history": self.move_history,
            "move_hist_save": self.move_hist_save,
            "move_counter": self.move_counter,
            "turn_number": self.turn_number,
            "noloss_turns": self.noloss_turns,
            "noloss_moves": self.noloss_moves,
            }
        return stats

    def get_current_stats_for_leaf(self) -> Dict[str, Any]:
        """
        creates a dictionary containing the necessary paramters to initiate a
        leaf copy for MCTS of this class instance. A leaf copy does not need to
        store moves, so these parameters are just 'disabled'
        
        Returns: dict, containing the parameter to initiate a leaf copy for
            MCTS of this class instance
        """
        stats = {
            "board": self.board,
            "black_tomove": self.black_tomove,
            "move_history": [],
            "move_hist_save": False,
            "move_counter": self.move_counter,
            "turn_number": self.turn_number,
            "noloss_turns": self.noloss_turns,
            "noloss_moves": self.noloss_moves,
            }
        return stats

    def get_current_board_losses(self) -> Tuple[np.ndarray, int, int]:
        """
        provides the current board state and the number of marbles lost by
        each color
        
        Returns:
            board: np.ndarray, current board state of the game
            black_loss: int, number of black marbles lost
            white_loss: int, number of white marbles lost
        """
        return self.board, self.black_loss, self.white_loss

    def get_current_state_reversed(self) -> np.ndarray:
        """
        provides the current board state from the view of the player who is to
        move next. This means, that the position is presented such that the
        white marbles will be moved next
        
        Returns: np.ndarray, current board state from the view of the current
            player (so if it white was the active player to move)
        """
        if self.black_tomove:
            return self.rotate_board(self.board)
        return self.board

    def calc_possible_moves(
            self,
            return_reversed: bool = True
            ) -> List[np.ndarray]:
        """
        provides a list of all possibly reachable board positions. This
        includes positions where the active player pushes the own marbles off
        the board. This function is rather used for experimenting.

        Args:
            return_reversed: Boolean, (defaults to True). If true the marbles
                which have to be moved next will be white. Otherwise all coming
                positions will be returned with the 'true' colors
            
        Returns: List[np.ndarray], list of all possibly reachable board 
            positions
        """
        # needs reworking
        new_states = []
        moved_offboard = set()
        bstate = np.array(self.board, dtype=np.int16)
        if self.black_tomove:
            bstate = self.rotate_board(bstate)

        marbles = np.argwhere(bstate == 1)
        for marble in marbles:
            for md in MOVE_DIRECTIONS:
                newpos_x, newpos_y = marble + md
                ### First: in-line moves ###
                # check offboard
                if bstate[newpos_x, newpos_y] == 3:
                    # 1st: for single marble move
                    # --> processed with broadside moves

                    # 2nd: for two marbles move
                    # checks whether there is a marble in opposite direction
                    mb_x, mb_y = marble - md
                    mb_pos = (mb_x, mb_y)
                    if bstate[mb_x, mb_y] == 1:
                        pos_state = np.array(bstate, dtype=np.int16)
                        pos_state[mb_x, mb_y] = 0
                        if mb_pos not in moved_offboard:
                            moved_offboard.update([mb_pos])
                            new_states.append(pos_state)

                        # 3rd: for three marble move
                        # checks for marble two fields in opposit direction
                        mbb_x, mbb_y = marble - 2 * md
                        mbb_pos = (mbb_x, mbb_y)
                        if bstate[mbb_x, mbb_y] == 1:
                            pos_state = np.array(bstate, dtype=np.int16)
                            pos_state[mbb_x, mbb_y] = 0
                            if mbb_pos not in moved_offboard:
                                moved_offboard.update([mbb_pos])
                                new_states.append(pos_state)

                # check empty field
                elif bstate[newpos_x, newpos_y] == 0:
                    # 1st: for single marble move
                    # --> processed with broadside moves

                    # 2nd: for two marbles move
                    # checks whether there is a marble in opposite direction
                    mb_x, mb_y = marble - md
                    if bstate[mb_x, mb_y] == 1:
                        pos_state = np.array(bstate, dtype=np.int16)
                        pos_state[mb_x, mb_y] = 0
                        pos_state[newpos_x, newpos_y] = 1
                        new_states.append(pos_state)

                        # 3rd: for three marble move
                        # checks for marble two fields in opposit direction
                        mbb_x, mbb_y = marble - 2 * md
                        if bstate[mbb_x, mbb_y] == 1:
                            pos_state = np.array(bstate, dtype=np.int16)
                            pos_state[mbb_x, mbb_y] = 0
                            pos_state[newpos_x, newpos_y] = 1
                            new_states.append(pos_state)

                # check opponent's marble
                elif bstate[newpos_x, newpos_y] == 2:
                    # 1st: for single marble move NOT possbile

                    # 2nd: for two marbles push (2 vs 1)
                    # checks whether there is a marble in opposite direction
                    mb_x, mb_y = marble - md
                    # for some cases an additional marble is needed
                    mbb_x, mbb_y = marble - 2 * md
                    if bstate[mb_x, mb_y] == 1:
                        # checks for offboard field behind target
                        t_x, t_y = marble + 2 * md
                        if bstate[t_x, t_y] == 3:
                            pos_state = np.array(bstate, dtype=np.int16)
                            pos_state[mb_x, mb_y] = 0
                            pos_state[newpos_x, newpos_y] = 1
                            new_states.append(pos_state)

                            # 3rd: for three marbles push (3 vs 1)
                            # checks for marble two fields in opposit direction
                            mbb_x, mbb_y = marble - 2 * md
                            if bstate[mbb_x, mbb_y] == 1:
                                pos_state = np.array(bstate, dtype=np.int16)
                                pos_state[mbb_x, mbb_y] = 0
                                pos_state[newpos_x, newpos_y] = 1
                                new_states.append(pos_state)

                        # checks for empty field behind target
                        elif bstate[t_x, t_y] == 0:
                            pos_state = np.array(bstate, dtype=np.int16)
                            pos_state[mb_x, mb_y] = 0
                            pos_state[newpos_x, newpos_y] = 1
                            pos_state[t_x, t_y] = 2
                            new_states.append(pos_state)

                            # 3rd: for three marbles push (3 vs 1)
                            # checks for marble two fields in opposit direction
                            if bstate[mbb_x, mbb_y] == 1:
                                pos_state = np.array(bstate, dtype=np.int16)
                                pos_state[mbb_x, mbb_y] = 0
                                pos_state[newpos_x, newpos_y] = 1
                                pos_state[t_x, t_y] = 2
                                new_states.append(pos_state)

                        # checks for 3 vs 2 push
                        elif (
                            bstate[t_x, t_y] == 2 and
                            bstate[mbb_x, mbb_y] == 1
                        ):
                            # checks for offboard field behind 2nd target
                            tt_x, tt_y = marble + 3 * md
                            if bstate[tt_x, tt_y] == 3:
                                pos_state = np.array(bstate, dtype=np.int16)
                                pos_state[mbb_x, mbb_y] = 0
                                pos_state[newpos_x, newpos_y] = 1
                                new_states.append(pos_state)

                            # checks for empty field behind 2nd target
                            elif bstate[tt_x, tt_y] == 0:
                                pos_state = np.array(bstate, dtype=np.int16)
                                pos_state[mbb_x, mbb_y] = 0
                                pos_state[newpos_x, newpos_y] = 1
                                pos_state[tt_x, tt_y] = 2
                                new_states.append(pos_state)

                ### Second: broadside moves ###
                for m, mb in enumerate(MOVE_BROADSIDES[tuple(md)]):
                    # there is some redundancy with "in-line" single moves
                    pos_state = np.array(bstate, dtype=np.int16)
                    offboard_all = True
                    to_move = []
                    for p in range(0, self.multi_move):
                        p_x, p_y = marble + p * mb
                        if bstate[p_x, p_y] == 1:
                            t_x, t_y = marble + p * mb + md
                            if bstate[t_x, t_y] == 3:
                                pos_state[p_x, p_y] = 0
                            elif bstate[t_x, t_y] == 0:
                                pos_state[p_x, p_y] = 0
                                pos_state[t_x, t_y] = 1
                                offboard_all = False
                            else:
                                break
                            to_move.append(p_x)
                            to_move.append(p_y)
                            if m > 0 and p == 0:
                                continue  # single marble move only once
                            elif not offboard_all:
                                new_states.append(
                                    np.array(pos_state, dtype=np.int16))
                            elif tuple(to_move) not in moved_offboard:
                                moved_offboard.update([tuple(to_move)])
                                new_states.append(
                                    np.array(pos_state, dtype=np.int16))
                        else:
                            break

        if not return_reversed and self.black_tomove:
            return [self.rotate_board(s) for s in new_states]

        return new_states

    def calc_nonlosing_moves(
            self,
            return_reversed: bool = True
            ) -> Tuple[List[np.ndarray], List[int]]:
        """
        provides a list of all possibly reachable board positions and a list
        with the corresponding move IDs. Here only positions are considired
        which are no a result of pushing an own marble off the board. The move
        IDs are used for agent to make predictions for the next move.

        Args:
            return_reversed: Boolean, (defaults to True). If true the marbles
                which have to be moved next will be white. Otherwise all coming
                positions will be returned with the 'true' colors
            
        Returns: 
            new_states: List[np.ndarray], list of all possibly reachable board 
                positions
            move_ids: List[int], corresponding move ID in order to reach the
                new positions from the current one. The move_ids will not be 
                reversed for 'return_reversed' == False
        """
        new_states = []
        move_ids = []
        bstate = np.array(self.board, dtype=np.int16)
        if self.black_tomove:
            bstate = self.rotate_board(bstate)

        marbles = np.argwhere(bstate == 1)
        for marble in marbles:
            for md in MOVE_DIRECTIONS:
                md_x, md_y = md
                newpos = marble + md
                newpos_x, newpos_y = newpos
                ### First: in-line moves ###
                if bstate[newpos_x, newpos_y] == 0:
                    # 1st: for single marble move
                    # --> processed with broadside moves

                    # 2nd: for two marbles move
                    # checks whether there is a marble in opposite direction
                    mb = marble - md
                    mb_x, mb_y = mb
                    if bstate[mb_x, mb_y] == 1:
                        pos_state = np.array(bstate, dtype=np.int16)
                        pos_state[mb_x, mb_y] = 0
                        pos_state[newpos_x, newpos_y] = 1
                        new_states.append(pos_state)
                        move_ids.append(MOVE_IDS[";".join(
                            [str(v) for v in [mb_x, mb_y, md_x, md_y]])])

                        # 3rd: for three marble move
                        # checks for marble two fields in opposit direction
                        mbb = marble - 2 * md
                        mbb_x, mbb_y = mbb
                        if bstate[mbb_x, mbb_y] == 1:
                            pos_state = np.array(bstate, dtype=np.int16)
                            pos_state[mbb_x, mbb_y] = 0
                            pos_state[newpos_x, newpos_y] = 1
                            new_states.append(pos_state)
                            move_ids.append(MOVE_IDS[";".join(
                                [str(v) for v in [mbb_x, mbb_y, md_x, md_y]])])

                # check opponent's marble
                elif bstate[newpos_x, newpos_y] == 2:
                    # 1st: for single marble move NOT possbile

                    # 2nd: for two marbles push (2 vs 1)
                    # checks whether there is a marble in opposite direction
                    mb_x, mb_y = marble - md
                    # for some cases an additional marble is needed
                    mbb_x, mbb_y = marble - 2 * md
                    if bstate[mb_x, mb_y] == 1:
                        # checks for offboard field behind target
                        t_x, t_y = marble + 2 * md
                        if bstate[t_x, t_y] == 3:
                            pos_state = np.array(bstate, dtype=np.int16)
                            pos_state[mb_x, mb_y] = 0
                            pos_state[newpos_x, newpos_y] = 1
                            new_states.append(pos_state)
                            move_ids.append(MOVE_IDS[";".join(
                                [str(v) for v in [mb_x, mb_y, md_x, md_y]])])

                            # 3rd: for three marbles push (3 vs 1)
                            # checks for marble two fields in opposit direction
                            if bstate[mbb_x, mbb_y] == 1:
                                pos_state = np.array(bstate, dtype=np.int16)
                                pos_state[mbb_x, mbb_y] = 0
                                pos_state[newpos_x, newpos_y] = 1
                                new_states.append(pos_state)
                                move_ids.append(MOVE_IDS[";".join(
                                    [str(v) for v in [mbb_x, mbb_y, md_x, md_y]
                                     ])])

                        # checks for empty field behind target
                        elif bstate[t_x, t_y] == 0:
                            pos_state = np.array(bstate, dtype=np.int16)
                            pos_state[mb_x, mb_y] = 0
                            pos_state[newpos_x, newpos_y] = 1
                            pos_state[t_x, t_y] = 2
                            new_states.append(pos_state)
                            move_ids.append(MOVE_IDS[";".join(
                                [str(v) for v in [mb_x, mb_y, md_x, md_y]])])

                            # 3rd: for three marbles push (3 vs 1)
                            # checks for marble two fields in opposit direction
                            if bstate[mbb_x, mbb_y] == 1:
                                pos_state = np.array(bstate, dtype=np.int16)
                                pos_state[mbb_x, mbb_y] = 0
                                pos_state[newpos_x, newpos_y] = 1
                                pos_state[t_x, t_y] = 2
                                new_states.append(pos_state)
                                move_ids.append(MOVE_IDS[";".join(
                                    [str(v) for v in [mbb_x, mbb_y, md_x, md_y]
                                     ])])

                        # checks for 3 vs 2 push
                        elif (
                            bstate[t_x, t_y] == 2 and
                            bstate[mbb_x, mbb_y] == 1
                        ):
                            # checks for offboard field behind 2nd target
                            tt_x, tt_y = marble + 3 * md
                            if bstate[tt_x, tt_y] == 3:
                                pos_state = np.array(bstate, dtype=np.int16)
                                pos_state[mbb_x, mbb_y] = 0
                                pos_state[newpos_x, newpos_y] = 1
                                new_states.append(pos_state)
                                move_ids.append(MOVE_IDS[";".join(
                                    [str(v) for v in [mbb_x, mbb_y, md_x, md_y]
                                     ])])

                            # checks for empty field behind 2nd target
                            elif bstate[tt_x, tt_y] == 0:
                                pos_state = np.array(bstate, dtype=np.int16)
                                pos_state[mbb_x, mbb_y] = 0
                                pos_state[newpos_x, newpos_y] = 1
                                pos_state[tt_x, tt_y] = 2
                                new_states.append(pos_state)
                                move_ids.append(MOVE_IDS[";".join(
                                    [str(v) for v in [mbb_x, mbb_y, md_x, md_y]
                                     ])])

                ### Second: broadside moves ###
                for m, mb in enumerate(MOVE_BROADSIDES[tuple(md)]):
                    # there is some redundancy with "in-line" single moves
                    pos_state = np.array(bstate, dtype=np.int16)
                    to_move = []
                    for p in range(0, self.multi_move):
                        p_x, p_y = marble + p * mb  # ursprungsposition
                        if bstate[p_x, p_y] == 1:
                            t_x, t_y = marble + p * mb + md  # zielposition
                            if bstate[t_x, t_y] == 0:  # nur freies Feld
                                pos_state[p_x, p_y] = 0
                                pos_state[t_x, t_y] = 1
                            else:
                                break
                            to_move.append(p_x)
                            to_move.append(p_y)
                            if m > 0 and p == 0:
                                continue  # single marble move only once

                            new_states.append(
                                np.array(pos_state, dtype=np.int16))
                            move_ids.append(MOVE_IDS[";".join(
                                [str(v) for v in to_move + [md_x, md_y]])])
                        else:
                            break

        if not return_reversed and self.black_tomove:
            return [self.rotate_board(s) for s in new_states], move_ids

        return new_states, move_ids

    def get_next_outcomes(
            self,
            pos_states: List[np.ndarray],
            get_reversed: bool = True) -> np.ndarray:
        """
        provides whether the next states result in a win, loss or draw

        Args:
            pos_states: List[np.ndarray], list of all possibly reachable states
                from the current positions
            get_reversed: Boolean, (defaults to True). Whether or not the
                possible states are provided from the view of the current
                player to move

        Returns: np.ndarray, 2-dimensional array, first dimensions contains the
            whether the next state is either a win for black or white and
            second dimension states whether the move will result in a draw
        """
        # scores / draw for every states
        outcomes = np.zeros((2, len(pos_states)), dtype=np.float32)
        outcomes[1, :] = 1
        if get_reversed and self.black_tomove:
            pos_states = [self.rotate_board(s) for s in pos_states]

        for p, pstate in enumerate(pos_states):
            white_loss = self.marble_max - np.sum(np.where(pstate == 1, 1, 0))
            if white_loss >= self.marble_loss_end:
                outcomes[0, p] = -1
                continue
            black_loss = self.marble_max - np.sum(np.where(pstate == 2, 1, 0))
            if black_loss >= self.marble_loss_end:
                outcomes[0, p] = 1
                continue

            if self.noloss_moves >= self.noloss_draw - 1:
                outcomes[1, p] = 0
                continue

            if self.reps_to_draw > 0:
                state_count = self.move_counter[tuple(pstate.flatten())]
                if state_count >= self.reps_to_draw:
                    outcomes[1, p] = 0
            elif self.center_win > 0:
                if self.noloss_turns >= self.center_win:
                    central_field = self.board[self.hex_side-1, self.hex_side-1]
                    if central_field == 1:
                        outcomes[0, p] = 1
                    elif central_field == 2:
                        outcomes[0, p] = -1
                elif (
                    self.noloss_turns >= self.center_win - 1 and
                    self.black_tomove is False
                ):
                    central_field = self.board[self.hex_side-1, self.hex_side-1]
                    if central_field == 1:
                        outcomes[0, p] = 1
                    elif central_field == 2:
                        outcomes[0, p] = -1

        return outcomes

    def set_board_state(
            self,
            new_state: np.ndarray,
            get_reversed: bool = True) -> None:
        """
        obtains the chosen, next state for the game and updates all variables.
        Also it is checked whether the game will be ended by the upcoming
        state. IMPORTANT: This function will not check whether the chosen state
        is legally reachable.
        
        Args:
            new_state: np.ndarray, the chosen, next state from white's 
                perspective
            get_reversed: bool, if True the 'new_state' will be obtained from
                white's perspective and has to be rotated
        """

        if self.black_tomove and get_reversed:
            new_state = self.rotate_board(new_state)

        self.board = new_state
        state_rep = tuple(new_state.flatten())
        self.move_counter[state_rep] += 1

        noloss = True
        white_count = np.sum(np.where(new_state == 1, 1, 0))
        white_newloss = self.marble_max - white_count
        if white_newloss > self.white_loss:
            self.white_loss = white_newloss
            noloss = False
        black_count = np.sum(np.where(new_state == 2, 1, 0))
        black_newloss = self.marble_max - black_count
        if black_newloss > self.black_loss:
            self.black_loss = black_newloss
            noloss = False

        if self.black_tomove:
            self.black_tomove = False
        else:
            self.black_tomove = True
            self.turn_number += 1

        if noloss:
            self.noloss_moves += 1
            if not self.black_tomove and self.noloss_moves > 1:
                self.noloss_turns += 1
        else:
            self.noloss_turns = 0
            self.noloss_moves = 0

        self.check_game_ended(state_rep)
        if self.move_hist_save:
            self.move_history.append(new_state)

    @staticmethod
    def rotate_board(board: np.ndarray) -> np.ndarray:
        """
        rotates the board and changes color, such that it seems the next player
        to make a move is the one with the white marbles
        
        Args:
            board: np.ndarray, the board to be adjusted

        Returns: np.ndarray, the board as if it was white to play
        """
        board = np.flip(np.flip(board, 1), 0)
        board = np.where(board == 2, 4, board)
        board = np.where(board == 1, 2, board)
        board = np.where(board == 4, 1, board)
        return board

    @staticmethod
    def represent_board_colored(board: np.ndarray) -> None:
        """
        prints out the given board color coded
        
        Args:
            board: np.ndarray, any board state
        """
        print("  ", end=" ")
        for val in range(11):
            print(Fore.GREEN+str(val), end=" ")
        print()
        for r, row in enumerate(board):
            print(Fore.GREEN+f"{r:>2}", end=" ")
            for t, tile in enumerate(row):
                if tile == 3:
                    print(Style.RESET_ALL+"+", end=" ")
                elif tile == 2:
                    print(Fore.BLUE+"@", end=" ")
                elif tile == 1:
                    print(Fore.YELLOW+"@", end=" ")
                else:
                    print(Style.RESET_ALL+"o", end=" ")
            print()

    @staticmethod
    def represent_board_nocol(board: np.ndarray) -> None:
        """
        prints out the given board without color coding
        
        Args:
            board: np.ndarray, any board state
        """
        print("  ", end=" ")
        for val in range(11):
            print(str(val), end=" ")
        print()
        for r, row in enumerate(board):
            print(f"{r:>2}", end=" ")
            for t, tile in enumerate(row):
                if tile == 3:
                    print("+", end=" ")
                elif tile == 2:
                    print("B", end=" ")
                elif tile == 1:
                    print("Y", end=" ")
                else:
                    print("o", end=" ")
            print()

    def represent_self(self) -> None:
        """
        prints out the current state
        """
        self.represent_board_nocol(self.board)

    def check_game_ended(self, current_rep) -> None:
        """
        internally checks whether the game has ended (win / loss / draw) and
        adjusts the corresponding values
        """
        if self.white_loss >= self.marble_loss_end:
            self.game_ended = True
            self.result = -1
        elif self.black_loss >= self.marble_loss_end:
            self.game_ended = True
            self.result = 1
        elif (self.noloss_turns >= self.noloss_draw or
              self.move_counter[current_rep] >= self.reps_to_draw):
            self.game_ended = True
            self.result = 0

    def check_future_draw(self, board: np.ndarray) -> bool:
        """
        checks whether the given state will result in a draw
        
        Args:
            board: np.ndarray, possible next state
        """
        if self.move_counter[tuple(board.flatten())] >= self.reps_to_draw - 1:
            return True
        return False

    def set_game_end(self, result):
        if result not in {-1, 0, 1}:
            return
        self.result = result
        self.game_ended = True

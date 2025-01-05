# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 08:07:07 2022

@author: hlocke
"""

from .board import Board
from copy import deepcopy
from . import constants as const
from .player_ai import MagisterPlay
import pygame as pg
from . import display as dsp
from .model_ai import get_trained_magister_zero
import numpy as np
from typing import List, Dict, Any, Union
from datetime import datetime

import os
# Manually places the window
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
SNAP_FOLDER = os.path.join(os.path.dirname(__file__), "snapshots")


ROW_OFFSET = [4, 3, 2, 1, 0, 0, 0, 0, 0]
ROW_LENGTH = [5, 6, 7, 8, 9, 8, 7, 6, 5]


class GameAI(Board):
    """
    board representation for pygame
    
    This GUI is based on the following repository
    https://github.com/a-pineau/Abalon3
    This GUI was used and modified with the agreement of the author.
    
    Args:
        configuration: str or List[List[int]], (defaults to classical Abalone
            starting position). Either provide the name of the position or the
            position directly as a list of lists. The outer list contains the
            rows, and the inner lists cotain the marlbe position within the
            rows. Possible position names are 'classic'/'standard',
            'belgiandaisy', 'germandaisy', 'swissdaisy', 'dutchdaisy',
            'domination', 'pyramid', 'wall'
        player_blue: Dict[str, Any], configuration for player "blue"
            type: str, 'human' or 'ai', (defaults to 'human'), required
            mcts_number: int, number of simulations for the AI player,
                (defaults to 250), only required if 'type' == 'ai'
            mcts_depth: int, moves made within every simulation. If 0, all
                simulations will be played until the end. (defaults to 13)
                Only required if 'type' == 'ai'
            prob_sum: float, for choosing moves for simulations only the moves
                with the highest probabilities summing up to 'prob_sum' will
                be considered. Values between 0.9 and 1.0 are suggested,
                (defaults to 0.95). Only required if 'type' == 'ai'
        player_yellow: Dict[str, Any], configuration for player "yellow"
            type: str, 'human' or 'ai', (defaults to 'human'), required
            mcts_number: int, number of simulations for the AI player,
                (defaults to 250), only required if 'type' == 'ai'
            mcts_depth: int, moves made within every simulation. If 0, all
                simulations will be played until the end. (defaults to 13)
                Only required if 'type' == 'ai'
            prob_sum: float, for choosing moves for simulations only the moves
                with the highest probabilities summing up to 'prob_sum' will
                be considered. Values between 0.9 and 1.0 are suggested,
                (defaults to 0.95). Only required if 'type' == 'ai'
    """
    def __init__(self,
                 configuration: Union[str, List[List[int]]] = const.STANDARD,
                 player_blue: Dict[str, Any] = const.DEFAULT_PLAYER,
                 player_yellow: Dict[str, Any] = const.DEFAULT_PLAYER):
        if isinstance(configuration, str):
            configuration = const.CONFIGURATIONS.get(
                configuration, const.STANDARD)
        super(GameAI, self).__init__(configuration)
        self.init_conf = deepcopy(configuration)

        self.current_human = True
        self.current_player = None

        self.ai_players = []
        if player_blue.get(const.PLAYER_TYPE, const.HUMAN) == const.AI:
            self.pblue_human = False
            self.pblue = self._setup_ai(player_blue)
            self.ai_players.append(self.pblue)
        else:
            self.pblue_human = True
            self.pblue = None

        if player_yellow.get(const.PLAYER_TYPE, const.HUMAN) == const.AI:
            self.pyellow_human = False
            self.pyellow = self._setup_ai(player_yellow)
            self.ai_players.append(self.pyellow)
        else:
            self.pyellow_human = True
            self.pyellow = None

    def _setup_ai(self, ai_config) -> MagisterPlay:
        model = get_trained_magister_zero()
        ai = MagisterPlay(
            model,
            self._board_into_array(),
            ai_config.get(const.PROB_SUM, const.PROB_SUM_DEFAULT),
            ai_config.get(const.MCTS_NUMBER, const.MCTS_NUMBER_DEFAULT),
            ai_config.get(const.MCTS_DEPTH, const.MCTS_DEPTH_DEFAULT))
        return ai

    def check_current_human(self) -> None:
        """
        Checks whether the player to move is a human player and changes
        the instances value depending on it
        """
        if self.current_color == 3:
            self.current_player = self.pyellow
            if self.pyellow_human:
                self.current_human = True
            else:
                self.current_human = False
        else:
            self.current_player = self.pblue
            if self.pblue_human:
                self.current_human = True
            else:
                self.current_human = False

    def _board_into_array(self):
        positions = np.ones((11, 11), dtype=np.int16) * 3
        for r, row in enumerate(self.data, 1):
            for c, value in enumerate(row, 1):
                positions[r, c+ROW_OFFSET[r-1]] = const.PG2AI[value]
        return positions

    def array_into_board(
            self,
            board:np.ndarray,
            black_loss: int,
            white_loss: int) -> None:
        """
        internally converts the array representation of the board into the one
        for the GUI
        
        Args:
            board: np.ndarray, 11 x 11 array with the board state
            black_loss: int, number of black marbles lost in the last move
            white_loss: int, number of white marbles lost in the last move
        """
        board = board[1:-1, 1:-1]
        for r, row in enumerate(board):
            for c, value in enumerate(row[ROW_OFFSET[r]:ROW_OFFSET[r]+ROW_LENGTH[r]]):
                pg_val = const.AI2PG[value]
                if self.data[r][c] != pg_val:
                    self.new_marbles[(r, c)] = pg_val
        if black_loss > 0:
            self.buffer_dead_marble[(0, 0)] = -2
        elif white_loss > 0:
            self.buffer_dead_marble[(0, 0)] = -3

    def update_ai(self) -> None:
        """
        Sends the new board state to the opposing AI player. So if blue moved
        last, yellow's board state will be updated and vice versa.
        """
        self.update()
        self.check_current_human()

        if self.current_player == self.pyellow and not self.pyellow_human:
            self.pyellow.make_given_move(self._board_into_array())

        if self.current_player == self.pblue and not self.pblue_human:
            self.pblue.make_given_move(self._board_into_array())

    def ai_move(self) -> None:
        """
        this function tells any AI player to make its move. If it is not an
        AI player to move, nothing happens.
        """
        if self.current_human:
            return

        _, old_bl, old_wl = self.current_player.get_current_board_losses()
        new_state, new_bl, new_wl = self.current_player.make_ai_move()

        self.array_into_board(new_state, new_bl-old_bl, new_wl-old_wl)
        # if it is AI vs AI, this is necessary
        self.update_ai()
        self.clear_buffers()

    def reset_ai(self) -> None:
        """
        resets the game to its initial board state
        """
        self.reset(self.init_conf())
        for ai in self.ai_players:
            ai.reset(self._board_into_array())
        self.check_current_human()

    def start_game(self) -> None:
        """Implements the game loop and handles the user's events"""
        pg.init()
        screen = pg.display.set_mode([const.WIDTH, const.HEIGHT])
        pg.display.set_caption("Abalon3")
        self.check_current_human()
        record = False
        running = True
        moving = False
        game_over = False
        valid_move = False

        while running:
            # Events handling
            for event in pg.event.get():
                mouse = pg.mouse.get_pos()
                p_keys = pg.key.get_pressed()
                p_mouse = pg.mouse.get_pressed()
                # Quiting game
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    # Quiting game with q
                    if event.key == pg.K_q:
                        running = False
                    # Confirming move and possible update
                    elif event.key == pg.K_SPACE:
                        moving = False
                        if valid_move:
                            self.update_ai()
                        game_over = self.check_win()
                        self.clear_buffers()
                    # Resetting game
                    elif event.key == pg.K_r:
                        self.reset_ai()
                        game_over = False
                # Selecting a single marble
                if not game_over and self.current_human:
                    if event.type == pg.MOUSEBUTTONDOWN and not p_keys[pg.K_LSHIFT]:
                        pick = self.normalize_coordinates(pg.mouse.get_pos())
                        # Checking pick validity 
                        # Cant be out of bounds or must be current color
                        if not pick or pick and self.get_value(pick) != self.current_color:
                            continue
                        # Move is valid, getting marble's data
                        moving = True
                        pick_center = self.get_center(pick)
                        moving_marble = const.MARBLE_IMGS[self.get_value(pick)].get_rect()
                        moving_marble.center = pick_center
                    # Releasing selection
                    elif event.type == pg.MOUSEBUTTONUP:
                        moving = False
                        self.clear_buffers()
                    # Moving single marble
                    elif event.type == pg.MOUSEMOTION and moving:
                        valid_move = False
                        moving_marble.move_ip(event.rel)
                        target = self.normalize_coordinates(mouse)
                        if not target:
                            continue # User's target is invalid (out of bounds)
                        # Valid target otherwise
                        target_center = self.get_center(target)
                        d = self.distance(pick_center, target_center)
                        # the target must be in the pick's neighborhood and cannot be the pick itself
                        if d <= const.MAX_DISTANCE_MARBLE and target != pick:
                            valid_move = self.push_marble(pick, target)
                    # Moving multiple marbles
                    elif p_keys[pg.K_LSHIFT] and p_mouse[0]:
                        pick = self.normalize_coordinates(mouse)
                        if not pick:
                            continue
                        value = self.get_value(pick)
                        centers = self.select_range(pick, value)
                        if centers:
                            valid_move = self.new_range(pick, centers)
            # Overall display
            dsp.overall_display(screen, self, game_over, valid_move)
            # Displaying the moving selected marble
            if moving: 
                origin_center = self.get_center(pick)
                rect_free = const.MARBLE_FREE.get_rect()
                rect_free.center = origin_center
                screen.blit(const.MARBLE_FREE, rect_free)
                screen.blit(const.MARBLE_IMGS[self.get_value(pick)], moving_marble)
            if record:
                record_game(screen)
            # Updating screen
            pg.display.update()
            # making an AI move
            self.ai_move()
        pg.quit()
        for ai in self.ai_players:
            ai.stop_execution()


def record_game(screen) -> None:
    """
    Save a snapshot of the current screen to the SNAP_FOLDER.

    Args:
        screen: pygame.Surface, Game window
    """
    n_snap = datetime.now().strftime("%Y%m%d-%H%M%S")
    extension = "png"
    file_name = f"snapshot_{n_snap}.{extension}"
    pg.image.save(screen, os.path.join(SNAP_FOLDER, file_name))

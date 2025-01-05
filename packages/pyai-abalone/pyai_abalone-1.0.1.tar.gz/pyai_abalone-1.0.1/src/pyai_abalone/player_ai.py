# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:35:05 2023

@author: hlocke
"""

from keras.utils.np_utils import to_categorical
from .abalone_ai import NumpyAbalone
from multiprocessing import Queue, cpu_count
import numpy as np
import random
import tensorflow as tf
import time
from threading import Thread
from typing import Optional, Tuple


class MagisterPlay():
    """
    AI player agent for abalone
    
    This AI agent is able to play Abalone. It is made to be run seperately from
    any abalone instance in order to make it more flexibly used. The agent uses
    MCTS in order to choose the next move.
    
    Args:
        model: tf.keras.Model, the model should take a one-hot encoded board
            state as input and output a distribution for all moves and an
            evaluation for the current provided state
        starting_position: np.ndarray, initial position to play the game from.
            This should be an acutal starting position with 14 marbles for each
            side
        prob_sum: float, (defaults to 0.95). The agent will only consider the
            predicted, best moves with the given probability sum. This is in
            order to avoid choosing inferior moves once and the by chance 
            selecting them although they are inferior
        num_mcts: int, (defaults to 100). Number of leafs to be considered for
            choosing the next move
        depth_mcts: int, (defaults to 0). The number of moves that the agent
            will make until it evaluates the position. If 0, the agent will
            play the leaf games until the end and use the final result for
            evaluation
        num_threads: int, (defaults to None): number of treads used for the
            MCTS. If None, threads according to the number of CPUs will be
            spawned
    """

    def __init__(self,
                 model: tf.keras.Model,
                 starting_position: np.ndarray,
                 prob_sum: float = 0.95,
                 num_mcts: int = 100,
                 depth_mcts: int = 0,
                 num_threads: Optional[int] = None):
        self.game = NumpyAbalone(starting_position)
        self.leaf_details = self.game.get_current_stats_for_leaf()

        self.prob_sum = prob_sum

        self.model = model
        self.num_mcts = num_mcts
        self.depth_mcts = depth_mcts
        self.move_queue = Queue()
        self.mcts_results = {}
        if num_threads is None:
            num_threads = cpu_count()
        self.num_threads = num_threads
        self.mcts_threads = []
        self._start_threads()

        for mt in self.mcts_threads:
            mt.daemon = True
            mt.start()

    def _start_threads(self):
        if self.mcts_threads:
            return

        if self.depth_mcts < 1:
            for _ in range(self.num_threads):
                self.mcts_threads.append(
                    Thread(target=self.mcts_full, args=()))
        else:
            for _ in range(self.num_threads):
                self.mcts_threads.append(
                    Thread(target=self.mcts_depth, args=()))

    def reset(self, starting_position: np.ndarray) -> None:
        """
        restarts the game with the given starting position
        
        Args:
            starting_position: np.ndarray, initial position to play the game
            from. This should be an acutal starting position with 14 marbles
            for each side
            
        """
        self.game = NumpyAbalone(starting_position)
        self._start_threads()

    def show_state(self, message: Optional[str] = None) -> None:
        """
        prints out a given message, the turn number, the current player to
        move, and a representation of the board state.
        
        Args:
            message: str, (defaults to None). Optional message to be printed
        """
        if message:
            print(message)
        to_move = "white"
        if self.game.black_tomove:
            to_move = "black"
        print(f"turn {self.game.turn_number} - {to_move} to move")
        self.game.represent_self()

    def make_ai_move(self) -> Tuple[np.ndarray, int, int]:
        """
        the AI agent will choose its next move based on the current game state.
        If the game has already ended, just the current board and marble
        losses will be returned
        
        Returns:
            board: np.ndarray, current board state of the game
            black_loss: int, number of black marbles lost
            white_loss: int, number of white marbles lost
        """
        if self.game.game_ended:
            return self.get_current_board_losses()

        self.leaf_details = self.game.get_current_stats_for_leaf()
        self.mcts_results = {}

        next_states, move_ids = self.game.calc_nonlosing_moves()
        next_ids = np.arange(len(next_states), dtype=np.int16)
        state_score = np.zeros(len(next_states), dtype=np.float32)
        state_played = np.zeros(len(next_states), dtype=np.float32)

        current_state = self.game.get_current_state_reversed()

        # one-hot encoding for the current state
        model_inp = to_categorical([current_state])
        # predicts logits and evaluation for the current state
        alogits, _ = self.model(model_inp)
        # calculates distribution for chossing a move for all possible moves
        chances = tf.nn.softmax(
            tf.gather(tf.squeeze(alogits), move_ids)).numpy()
        # adjust the probabilities according to the class variable 'prob_sum'
        chances = self._prob_sum_chances(chances)
        # chooses the next states for the MCTS leafs
        pos_states = random.choices(
            next_ids,
            weights=chances,
            k=self.num_mcts)

        # put the leaf states into the queue
        for m_idx, s_idx in enumerate(pos_states):
            self.move_queue.put((m_idx, s_idx, next_states[s_idx]))

        # wait until all leaf games were played to the desired depth
        while len(self.mcts_results) < self.num_mcts:
            time.sleep(0.1)

        # sum up the scores and times played for all unique leaf states
        for s_idx, score, in self.mcts_results.values():
            state_score[s_idx] += score
            state_played[s_idx] += 1

        # normalize scores to number of playing
        scores = state_score / np.where(
            state_played == 0, 1, state_played).astype(np.float32)
        # penalize unplayed states
        scores += np.where(state_played == 0, -2.0, 0).astype(np.float32)
        scores_bestid = np.argwhere(scores == np.amax(scores))

        # choose the state with the best averaged outcome
        chosen_id = np.argmax(chances[scores_bestid])
        chosen_id = scores_bestid.flatten()[chosen_id]
        chosen_state = next_states[chosen_id]
        # update the game state and check whether it ended
        self.game.set_board_state(chosen_state)
        self._check_game_ended()
        return self.get_current_board_losses()

    def make_given_move(
            self,
            chosen_state: np.ndarray
            ) -> Tuple[np.ndarray, int, int]:
        """
        sets the agents internal state to the provided one. The agent will
        return its own state representation and the respective color's losses
        
        Returns:
            board: np.ndarray, current board state of the game
            black_loss: int, number of black marbles lost
            white_loss: int, number of white marbles lost
        """
        if self.game.game_ended:
            return self.get_current_board_losses()

        self.game.set_board_state(chosen_state, get_reversed=False)
        self._check_game_ended()
        return self.get_current_board_losses()

    def mcts_full(self):
        """
        this method is called if the 'mcts_depth' variable is set to 0, such
        that all leaf games are played until the end. Every thread of the MCTS
        calls this method once, when the agent class is initiated. The method
        is run until the agent's main game is finished. After that all threads
        will be joined. Inside the methode one of the provided leaf games is 
        obtained and played until the end. Then its result is stored.
        """
        # as long as the main game is running this method and its corresponding
        # thread will run
        while not self.game.game_ended:
            # mcts_id is for storing the result later
            mcts_id, state_id, state = self.move_queue.get()
            # special mcts_id to join and end all threads
            if mcts_id == -1:
                break
            # creates a leaf game with the stored parameters
            m_game = NumpyAbalone(**self.leaf_details)
            # make one move to reach the provided leaf state to start from
            m_game.set_board_state(state)
            # play the game until the end
            while not m_game.game_ended:
                next_states, move_ids = m_game.calc_nonlosing_moves()
                current_state = m_game.get_current_state_reversed()

                model_inp = to_categorical([current_state])
                alogits, _ = self.model(model_inp)
                # create a probability distribution for the current position
                chances = tf.nn.softmax(
                    tf.gather(tf.squeeze(alogits), move_ids)).numpy()
                # randomly select one of the next states according to its
                # winning chance
                chosen_state = random.choices(next_states, weights=chances)[0]
                m_game.set_board_state(chosen_state)

            score = m_game.result
            # adjust the score depending on the actual side the agent plays for
            if self.game.black_tomove:
                score = -score

            self.mcts_results[mcts_id] = (state_id, score)

    def mcts_depth(self):
        """
        this method is called if the 'mcts_depth' variable is set to any number
        larger than zero and all leaf games will played until they end or that
        given number of moves is reached. Every thread of the MCTS
        calls this method once, when the agent class is initiated. The method
        is run until the agent's main game is finished. After that all threads
        will be joined. Inside the methode one of the provided leaf games is 
        obtained and will be played until it ends or that the given number of
        moves is reached. Then its result is stored.
        """
        # as long as the main game is running this method and its corresponding
        # thread will run
        while not self.game.game_ended:
            mcts_id, state_id, state = self.move_queue.get()
            # special mcts_id to join and end all threads
            if mcts_id == -1:
                break
            # creates a leaf game with the stored parameters
            m_game = NumpyAbalone(**self.leaf_details)
            # make one move to reach the provided leaf state to start from
            m_game.set_board_state(state)

            # one move was already done
            for _ in range(self.depth_mcts-1):
                next_states, move_ids = m_game.calc_nonlosing_moves()
                current_state = m_game.get_current_state_reversed()

                model_inp = to_categorical([current_state])
                alogits, _ = self.model(model_inp)
                chances = tf.nn.softmax(
                    tf.gather(tf.squeeze(alogits), move_ids)).numpy()
                chosen_state = random.choices(next_states, weights=chances)[0]
                m_game.set_board_state(chosen_state)

                if m_game.game_ended:
                    break

            score = m_game.result
            # if the lead game did not end yet, the model will be used
            if not m_game.game_ended:
                current_state = m_game.get_current_state_reversed()
                model_inp = to_categorical([current_state])
                _, val = self.model(model_inp)
                score = tf.squeeze(val).numpy()
                if m_game.black_tomove:
                    score = -score

            # adjust the score depending on the actual side the agent plays for
            if self.game.black_tomove:
                score = -score

            self.mcts_results[mcts_id] = (state_id, score)

    def get_current_board_losses(self):
        """
        provides the current board state and the number of marbles lost by
        each color for the agent's main game
        
        Returns:
            board: np.ndarray, current board state of the game
            black_loss: int, number of black marbles lost
            white_loss: int, number of white marbles lost
        """
        return self.game.get_current_board_losses()

    def _prob_sum_chances(self, chances):
        if self.prob_sum < 1.0:
            lowest_chance = 0.0
            chance_sum = 0.0
            chances_sorted = -np.sort(-chances)
            for chance in chances_sorted:
                chance_sum += chance
                if chance_sum >= self.prob_sum:
                    lowest_chance = chance
                    break
            chances = np.where(chances < lowest_chance, 0.0, chances)

        return chances

    def _check_game_ended(self):
        if not self.game.game_ended:
            return

        for _ in range(len(self.mcts_threads)):
            self.move_queue.put((-1, 0, []))

        for mt in self.mcts_threads:
            mt.join()
        self.mcts_threads = []

    def stop_execution(self):
        self.game.set_game_end(0)
        self._check_game_ended()

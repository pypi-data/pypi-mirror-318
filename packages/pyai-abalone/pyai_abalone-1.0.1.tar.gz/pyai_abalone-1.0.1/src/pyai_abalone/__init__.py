# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:09:38 2024

@author: hlocke
"""
__version__ = "1.0.1"

from .board_ai import GameAI
from .player_ai import MagisterPlay
from .abalone_ai import NumpyAbalone
from .model_ai import MagisterZero, get_trained_magister_zero
from . import starting_positions

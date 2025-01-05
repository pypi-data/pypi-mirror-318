# pyai_abalone

Author: Harald Locke <haraldlocke@gmx.de>

## Summary

Python Abalone AI based on Alpha-Zero concept

## Installation

```bash
pip install pyai_abalone
```

## Features

The package provides an implementation of the Abalone game using numpy, it is quite fast for Python.
It also contains an agent, that is able to play the game on its own applying Alpha-Zero concepts,
which means, that a image recognition AI architecture is coupled with Monte Carlo tree search.
Finally, it is possible to play against this AI agent via a GUI provided by [A. Pineau](https://github.com/a-pineau/Abalon3).

### Board representation

The board for all these implementations is represented by a numpy.ndarray with the following concepts

* The shape is `(11, 11)` in order to fit in all rows and an "edge" that is used to predict, when a marble is pushed off the board
* value `3` means "off-board" field. They are used to get the hexagonal shape and to savly calculate pushing marbles off the board
* value `2` is for black marbles
* value `1` is for white marbles. Note, that the AI always plays from the white perspective.
  This make it necessary to flip the board accordingly, which is implemented
* value `0` are just empty fields on the board

An example board is given bellow with the famous "Beglian Daisy" starting position

```python
import numpy as np
belgian_daisy = np.array([
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 1, 1, 0, 2, 2, 3],
    [3, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3],
    [3, 3, 3, 0, 1, 1, 0, 2, 2, 0, 3],
    [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
    [3, 0, 2, 2, 0, 1, 1, 0, 3, 3, 3],
    [3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 3],
    [3, 2, 2, 0, 1, 1, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]],
    dtype=np.int16)
```

### Modul import

All functionalities are bundled in one package

```python
import pyai_abalone
```

### Abalone implementation

```python
abalone = pyai_abalone.NumpyAbalone()

# this function is used by the agent to generate the possible moves
pot_states, move_ids = abalone.calc_nonlosing_moves()

# in order to make a move, provide the follow-up position to the game instance
# Note: the game will NOT check, whether the position is actually possible
abalone.set_board_state(pot_states[0])

# this function calculates every possible moves
# even if that means pushing the own marbles off the board
pot_states = abalone.calc_possible_moves()
```

### AI model

The Alpha-Zero model architecture architecture can be used directly.
The architecture is already fit to the Abalone implementation, which means it has an imput shape of `(11, 11, 4)`

```python
# untrained model
new_model = pyai_abalone.MagisterZero(
    num_resblocks=2,  # number of residual layers based on Conv2D layers
    filters=64,  # number of filters for the Conv2D layers
    num_actions=1506  # number of actions
)

# trained model, provide an isntance of 'MagisterZero' with trained weights
trained_model = pyai_abalone.get_train_magister_zero()
```

### AI Agent

The agent can be flexibly used with different models, they are just supposed to fit into the
Ablone implementation. So a model should have an input shape of `(11, 11, 4)` and has two
outputs. The first should return the logits for the possible `1506` actions, the second one
should provide an evaluation of the position.

```python
import numpy as np

agent = pyai_abalone.MagisterPlay(
    model=pyai_abalone.get_train_magister_zero(),
    starting_position=pyai_abalone.constants.BELGIAN_DAISY,
    prob_sum=0.95,
    num_mcts=20,
    depth_mcts=11,
    num_threads=4
    )

# hand over a follow-up state to the agent so that is adjusts its internal representation
# Note: the agent will expect to receive the state as it is and not from white's perspective
next_state = np.array([
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 1, 1, 0, 2, 2, 3],
    [3, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3],
    [3, 3, 3, 0, 1, 1, 0, 2, 2, 0, 3],
    [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 2, 0, 0, 0, 0, 3, 3],
    [3, 0, 2, 2, 0, 1, 1, 0, 3, 3, 3],
    [3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 3],
    [3, 0, 2, 0, 1, 1, 1, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    ],
    dtype=np.int16)

agent.make_given_move(next_state)

# the agent will perform MCTS and return the state after it made a move
new_state, black_loss, white_loss = agent.make_ai_move()
```

### Play against the agent

In order to play against the agent, there are two options to start a game:

#### Running the class in an own script

```python
game = pyai_abalone.GameAI()
game.start_game()
```

#### Run game_ai.py

After installation run the provided `game_ai.py` found in the package folder

```bash
python game_ai.py [-h] [-s <settings.json>] [-b <position>]
                  [--blue <player-type>] [--blue_mcts <integer>]
                  [--blue_depth <integer>] [--blue_probsum <float>]
                  [--yellow <player-type>] [--yellow_mcts <integer>]
                  [--yellow_depth <integer>] [--yellow_probsum <float>]
```

| option | description |
| --- | --- |
| -h, --help | show this help message and exit |
| -s \<settings.json\>, --settings  \<settings.json\> | .json-file containing the game setup. If provided, options will be primarily taken from that file. All settings not provided within the file, will be set to the other, given arguement values (or their default value if they were not specified at all) |
| -b \<position\>, --board \<position\> | chooses starting positions, available positions are: classic / standard, belgian_daisy, german_daisy, dutch_daisy, swiss_daisy, domination, pyramid, wall / the_wall (default: belgian_daisy) Note: The A.I. was mainly trained on the 'Beglian Daisy' position, so it might play much worse on the other starting positions |
| --blue \<player-type> | sets the player for the blue marbles to human or A.I., available options are: human, ai (default: human) |
| --blue_mcts \<integer\> | sets the number of Monte-Carlo tree searches performed at every move for the blue player (if it is an A.I). This drastically influences playing strength of the A.I, but also the time it needs to calculate for a move (default: 250) |
| --blue_depth \<integer\> | sets the depth of the MCTS search for the blue player (if it is an A.I). For every search the number of 'blue_depth' moves will be performed and the position evaluated afterwards (default: 13) |
| --blue_probsum \<float\> | For the root of the MCTS tree only the moves with the highest probabilities summing up to 'blue_probsum' will be considered. For all later nodes this restriction is not in place (default: 0.95) |
| --yellow \<player-type\> | sets the player for the yellow marbles to human or A.I., available options are: human, ai (default: ai) |
| --yellow_mcts integer> | sets the number of Monte-Carlo tree searches performed at every move for the yellow player (if it is an A.I). This drastically influences playing strength of the A.I, but also the time it needs to calculate for a move (default: 250) |
| --yellow_depth \<integer\> | sets the depth of the MCTS search for the yellow player if it is an A.I. For every search the number of 'yewllow_depth' moves will be performed and the position evaluated afterwards (default: 13) |
| --yellow_probsum \<float\> | For the root of the MCTS tree only the moves with the highest probabilities summing up to 'yewllow_probsum' will be considered. For all later nodes this restriction is not in place (default: 0.95) |

## GUI

The GUI was taken and modified from [Abalone3](https://github.com/a-pineau/Abalon3) with
the consent of the author.

## Scope & limitations

This is an implementation of an Alpha-Zero style agent for Abalone. It was trained on actual games provided by Vincent Frochot who is running [AbalOnline](https://abal.online/). Despite the algorithm being quite sound, the code is limited by Python's general slow speed and its GIL (genral interpreter lock) which prevents performance efficient threading. Thus the whole package can be rather seen as a prove of concept.

## Concept

The agent applies the concept of AlphaZero and uses Monte Carlo tree search to choose its move. Within the tree search an AI model
related to image recognition chooses the next moves.

## Further improvement

As it is hard to surpass Python's GIL and even more its speed a Rust implementation of this package was produced which can be found here

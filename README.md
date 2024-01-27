# TicTacToe

A console based tic-tac-toe program where the computer plays both X and O.

### TicTacToe.py 

This version is the first attempt at creating the game. It is completely random and it does not save any game information.

### TicTacToe_1.0.py 

This version records and ranks every move in both a winning and losing game when the positional choices are random. It then writes those results to a json file.

### TicTacToe_2.0.py

This version has two different use cases. 

1. A game with no previous data that records and ranks every move in both a winning and losing game when the positional choices are mostly random. The only exception to being a purely random game is that blocking an opponents winning move will take precendence over a higher ranked move. The result of the games outcome is then written to a json file, except in the event that the game is a draw.

2. A game that uses previous game data to pick the best move based off the highest ranked available position, which is only superseded by the need to block an opponents winning move. The result of the games outcome is then written to a json file, except in the event that the game is a draw.

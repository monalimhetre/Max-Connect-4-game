
NAME: Monali Mhetre

LANGUAGE: Python
 


STRUCTURE:

The game uses
 two python files:

maxconnect4.py contains all the functions related to game information like what input to take from user, 
calling ai related functions and setting up the board.

MaxConnect4Game.py contains all the functions related to implementing the algorithms of the game and also the evaluation function.

 
COMPILATION AND EXECUTION:



To run the code, execute maxconnect4.py with standard python compilation commands
For interactive mode, pass the following arguments:
	

python maxconnect4.py interactive [input_file] [computer-next/human-next] [depth]

	

For one-move mode, pass the following arguments:
	

python maxconnect4.py one-move [input_file] [output_file] [depth]


Note: Code runs on omega. It takes 4-5 minutes for execution.
 

REFERENCES:

Taken some reference to implement minimax alpha beta pruning from pseudocode given on

https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

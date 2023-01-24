# a_different_chess_python
# Weird Chess Game
A chess game with a few different rules.White pawns will only be able to move upwards (from 1 to 8) and black pawns will only be able to
move downwards. The two-square starting move of pawns will not be available. Also, there
will be one exception case for Knight. If the square is unoccupied, it can move on the same
closest diagonal square, too. Another exception is about moving Bishop.
The bishop can move on just forward according to its moving direction.<br />
## Commands:<br />
COMMAND-1: initialize<br />
Arguments: This command does not take any arguments.<br />
Description: This command load the pieces to the board.<br />
Output: OK<br />
COMMAND-2: showmoves<br />
Arguments: piece<br />
Description: Lists the possible target positions of the given piece can move. The order of
the positions will be from a to h and from 1 to 8 increasing, i.e. a3 will be printed before a5
and a7 will be printed before b2.<br />
Output: position1 position2 position3...<br />
Output on Failure: FAILED<br />
COMMAND-3: move<br />
Arguments: piece position<br />
Description: Moves the given piece to the given position. The operation should fail if the
move is not valid.<br />
Output on successful operation: OK<br />
Output on Failure: FAILED<br />
COMMAND-4: print<br />
Arguments: This command does not take any arguments.<br />
Description: Prints the status of the board to the console.<br />
Output: The output will be 8 lines of 8 characters, where the rows will be 8 to 1 from
top to bottom and the columns will be a to h from left to right. Pieces will be represented
with their corresponding letters and empty squares will be represented as a single whitespace
character.<br />
COMMAND-5: exit<br />
Arguments: This command does not take any arguments.<br />
Description: Instructs the program to exit.<br />
Output: This command does not output any information to the console.<br />

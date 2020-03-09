
from copy import deepcopy
import alphabeta
import sys
from MaxConnect4Game import *


def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    # currentGame.aiPlay() # Make a move (only random is implemented)
    value_of_a = alphabeta.alphabetadecision(currentGame)
    currentGame.playPiece(value_of_a)
    print 'Game state after move:'
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame , playerTurn):
    # Fill me in
    if playerTurn == 'human-first':
        currentGame.currentTurn = 2
    else:
        currentGame.currentTurn = 1
    while not currentGame.pieceCount == 42:
        if currentGame.currentTurn == 2:
            input_coloumn = int(raw_input('please enter coloums number between 0 to 6: '))
            while input_coloumn > 6:
                raw_input('please enter valid number between 0 to 6: ')
            currentGame.playPiece(input_coloumn)
            # currentGame.printGameBoard()
            currentGame.currentTurn = 1
            try:
                currentGame.gameFile = open('human.txt', 'w')
                # currentGame.printGameBoard()
                # currentGame.gameFile.write(currentGame.printGameBoard())
                # currentGame.gameFile.close()
            except:
                pass
                # sys.exit('exit from human.')

            # currentGame.aiPlay(input_coloumn)
        # deepcopy(currentGame.gameBoard)
        # interactiveGame(currentGame.gameBoard,currentGame.currentTurn)
        else:
            # if currentGame.pieceCount == 42:
            #     sys.exit('board is full.')
            # # call alphabeta and then call play piece function.
            # currentGame.aiPlay(sys.argv[4])
            currentGame.currentTurn = 2
            coloumn_number = alphabeta.alphabetadecision(currentGame)
            currentGame.currentTurn = 1
            currentGame.playPiece(coloumn_number)
            # currentGame.gameBoard
            # print('after executing iterative mode.')
            currentGame.currentTurn = 2
            try:
                currentGame.gameFile = open('computer.txt', 'w')
                # currentGame.printGameBoard()
                # currentGame.gameFile.close()
            except:
                pass
                # sys.exit('exit from computer end.')

        currentGame.printGameBoardToFile()
        currentGame.printGameBoard()
        currentGame.gameFile.close()
        # print('computer next board:\n ', currentGame.printGameBoard())
        currentGame.countScore()
        print('player1 score is: ', currentGame.player1Score , 'Player2 score is: ', currentGame.player2Score)
        # print()
        # else:
        # print(playerTurn,'player turn')
        # sys.exit('please choose human-next or computer-next.')
        #

def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)
    # store the game mode , input file , output file and depth.
    game_mode, inFile = argv[1:3]
    # depth = sys.argv[4]
    # player_turn = sys.argv[3]
    # print('player turn',player_turn)
    # # print 'game mode',game_mode,'input file',inFile,'output file',outFile,'depth',depth

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game
    currentGame.depth = int(sys.argv[4])
    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    # print 'file lines: ',file_lines
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    # print(currentGame.gameBoard)
    currentGame.currentTurn = int(file_lines[-1][0])
    # print 'current turn: ',currentGame.currentTurn
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    # print('check piece count: ', currentGame.checkPieceCount())
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        player_turn = sys.argv[3]
        file_not_found = True
        interactiveGame(currentGame,player_turn) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)




import numpy as np
import copy
import ast
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from threading import Thread



board = np.array([
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"],
])

print(f'{board} \n')



def selectPosition(board, position:int, player:str):
    if position in range(0,10,1):
        row = int((position-1) /3)
        column = (position-1)%3
        if board[row][column] == "X" or board[row][column] == "O":
            print("\nInvalid Position\n")
            return False
        board[row,column] = player
        return True

    else:
        print("Out of range selection")
        return False 

def has_won(board, player:str):
    win = None
    for move in range(3):
        checkColumn = board[:,move] == player
        checkRow = board[move,:] == player
        # print(f'CHECK ROW: {checkRow}')
        # print(f'CHECK Column: {checkColumn}')
        if checkColumn.all() or checkRow.all():
            win = True
            
            break
        else:
            continue    

    
    #Diagonal Check
    for check in range(0,3):
        if board[check,check] != player:
            win == False
            break
        if check == 2:
            win = True    
            
    for check in range(0,3):
        if board[check,abs(check-2)] != player:
            win == False
            break
        if check == 2:
            win = True     

    #Final Win Check 
    if win:
        # print(f"{player} has won!")
        return True
    else:
        # print(f"{player} has not won.")
        pass
    return False
            

def availableMoves(board):
    moves = []
    for row in board:
        for column in row:
            if column != "O" and column != "X":
                moves.append(column) 
    return moves

def isTie(board):
    if not has_won(board,"X") and not has_won(board,"O") and len(availableMoves(board)) == 0:
        return True
    else:
        return False

def gameEnded(board):
    return has_won(board,"X") or has_won(board,"O") or len(availableMoves(board)) == 0

def evaluateBoard(board):
    if has_won(board,"X"):
        # print(f"X has won the game!")
        return 1
    if has_won(board,"O"):
        # print(f"O has won the game!")
        return -1
    if len(availableMoves(board)) == 0:
        # print(f"The game is a tie!")
        return 0

def minimax(board, is_maximizing):

    # Base Case
    if gameEnded(board):
        return [evaluateBoard(board), ""]

    # # Maximizing Player
    if is_maximizing:
        bestValue = -float("Inf")
        bestMove = ""

        for move in availableMoves(board):
            boardCopy = copy.deepcopy(board)
            selectPosition(boardCopy, int(move), "X")

            hypotheticalValue = minimax(boardCopy, False)[0]

            if hypotheticalValue > bestValue:
                bestValue = hypotheticalValue
                bestMove = move
        return [bestValue,int(bestMove)]
    

    # Minimizing Player
    else:
        bestValue = float("Inf")
        bestMove = ""

        for move in availableMoves(board):
            boardCopy = copy.deepcopy(board)
            selectPosition(boardCopy, int(move), "O")

            hypotheticalValue = minimax(boardCopy, True)[0]

            if hypotheticalValue < bestValue:
                bestValue = hypotheticalValue
                bestMove = move
        
        return [bestValue,int(bestMove)]



def tictactoeGame():
    while not gameEnded(board):
        gameStatDict = {}
        validMove = False
        while not validMove:        
            userMove = None


            read = False
            while not read :
                # import fileWatch
                exec(open('fileWatch.py').read())
                with open('data.txt', 'r') as f:
                    gameStatDict = ast.literal_eval(f.read())
                    print(gameStatDict)
                    
                    
                    print(gameStatDict["UserMove"])
                    if selectPosition(board,int(gameStatDict["UserMove"]), "O"):
                        validMove = True
                    print("\n", board)
                    
                    print(f'Read UI Input: {gameStatDict["UserMove"]}')
                    read = True

        
        if gameEnded(board):
            result = evaluateBoard(board)
            gameStatDict["GameEnded"] = True

            if result == 1:
                gameStatDict["winner"] = " X "
            elif result == -1:
                gameStatDict["winner"] = " O "
            elif result == 0:
                gameStatDict["winner"] = "Tie"
            with open("data.txt", 'w') as f:
                f.write(str(gameStatDict))
            
            # board = np.array([
            # ["1","2","3"],
            # ["4","5","6"],
            # ["7","8","9"],
            # ])
            # tictactoeGame()
            
            break

        print("\nAI's Turn")

        gameStatDict["AIMove"] = minimax(board,True)[1]
        if selectPosition(board,gameStatDict["AIMove"], "X"):
            validMove = True
        print("\n", board)

        with open("data.txt", 'w') as f:
            f.write(str(gameStatDict))

        with open("data2.txt", 'w') as f:
         f.write("Modify Check File")


        # time = os.path.getmtime('data.txt')
    
        if gameEnded(board):
                result = evaluateBoard(board)
                gameStatDict["GameEnded"] = True

                if result == 1:
                    gameStatDict["winner"] = " X "
                elif result == -1:
                    gameStatDict["winner"] = " O "
                elif result == 0:
                    gameStatDict["winner"] = "Tie"
                with open("data.txt", 'w') as f:
                    f.write(str(gameStatDict))

                # tictactoeGame()


        


tictactoeGame()
    

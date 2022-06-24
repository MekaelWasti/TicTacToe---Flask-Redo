import numpy as np
import sys, os
import copy
import ast
# from app import sendME 
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from threading import Thread
import keyboard





# def fileWatcher():

#     # exitProgram = False

#     # FILE WATCHER
#     print("y e r o")
#     # def exitCheck(exitProgram):
#         # exitProgram = True
#         # return exitProgram

#     # if exitProgram == True:
#         # return True
    

#     if __name__ == "__main__":
#         patterns = ["*"]
#         ignore_patterns = None
#         ignore_directories = False
#         case_sensitive = True
#         my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

        
#     def userMove():
#         with open('data.txt', 'r') as f:
#             gameStatDict = f.readline()
#             # gameStatDict = f.readline()
#             gameStatDict = ast.literal_eval(gameStatDict)
#             # gameStatDict = eval(gameStatDict)
#             print(gameStatDict)
#             # gameStatDict = json.loads(gameStatDict)
#             print(gameStatDict["UserMove"])
#             print("Worked")


#     def on_modified(event):
#         if event.src_path == ".\data2.txt":
#             my_observer.stop()

#             print(my_observer.is_alive())

#             print("2")
#             print(my_observer.ident)

#             print(f"{event.src_path} has been modified")
#             # exitCheck(exitProgram)
#             # userMove()

    

#     my_event_handler.on_modified = on_modified
    
    

#     path = "."
#     go_recursively = True
#     my_observer = Observer()
#     my_observer.schedule(my_event_handler, path, recursive=go_recursively)


#     my_observer.start()
#     print("1")
#     print(my_observer.ident)
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         my_observer.stop()
#     my_observer.join()
#         # sys.exit(1)

    




# GAME
# thread = Thread(target=fileWatcher)
# thread.start()


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


        # validMove = False
        # while not validMove:
        #     userMove = int(input("Select a tile: "))
        #     if selectPosition(board,userMove, "O"):
        #         validMove = True
        #     print("\n", board)
        
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
    

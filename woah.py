from threading import Thread
import time

def tictactoeCall():
   exec(open('TicTacToeMinimax.py').read())

gameThread = Thread(target=tictactoeCall)
gameThread.start()

while True:
    time.sleep(1)
    print("test")
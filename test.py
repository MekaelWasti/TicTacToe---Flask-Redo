import os
import ast


while True:
    read = False
    time = os.path.getmtime('data1.txt')
    while not read :
        if (time != os.path.getmtime('data1.txt')):
            with open('data1.txt', 'r') as f:
                for line in f:
                    gameStatDict = ast.literal_eval(line)
                # gameStatDict = dict(f.read())
                    print(gameStatDict)
                    
                    
                    # print(gameStatDict["UserMove"])
                    
                    # print(f'Read UI Input: {gameStatDict["UserMove"]}')
                    read = True
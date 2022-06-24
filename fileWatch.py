import time
import ast
import os
import json
import sys

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

run = True

# if __name__ == "__main__":
patterns = ["*"]
ignore_patterns = None
ignore_directories = False
case_sensitive = True
my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)



def userMove():
    with open('data.txt', 'r') as f:
        gameStatDict = f.readline()
        # gameStatDict = f.readline()
        gameStatDict = ast.literal_eval(gameStatDict)
        # gameStatDict = eval(gameStatDict)
        print(gameStatDict)
        # gameStatDict = json.loads(gameStatDict)
        print(gameStatDict["UserMove"])
        print("Worked")

def on_modified(event):
    if event.src_path == ".\data2.txt":
        # userMove()
        global run
        run = False
        
    # print(f"{event.src_path} has been modified")


my_event_handler.on_modified = on_modified

path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
# try:
while run:
    time.sleep(1)

    if not run:
        print("broken")
        my_observer.stop()
        my_observer.join()
        break
        # sys.exit(0)
        # quit()
        # exit()

            # break
        
# except KeyboardInterrupt:
# except run == False or KeyboardInterrupt:
#     print('wow')
#     my_observer.stop()
# my_observer.join()

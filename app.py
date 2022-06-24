from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import os
import time
from threading import Thread
import subprocess


def tictactoeCall():
   exec(open('TicTacToeMinimax.py').read())
   # print("test1")

gameThread = Thread(target=tictactoeCall, args=())
gameThread.start()


# <strong>#Set up Flaskstrong>:
turnCount = 0



# <strong>#Set up Flaskstrong>:
time1 = -float("Inf")
app = Flask(__name__)
#Set up Flask to bypass CORS at the front end:
CORS(app)
# cors = CORS(app)



# @app.route("/",methods = ["POST", "GET"])
@app.route("/")
def home():
   # gameThread.start()
   gameCall = subprocess.Popen(['python', 'TicTacToeMinimax.py'])

   # gameThread.join()  
   return render_template('index.html')

# @app.route("/")
# def code():
   #  out = open(r'TicTacToeMinimax.py', 'r').read()
   #  return exec(out)


@app.route("/<usr>")
def usr(usr):
   return f'<h1>{usr}</h1>'

@app.route("/login")
def login():
   return render_template('index.html')



#Create the receiver API POST endpoint:
@app.route("/receiver", methods=["GET", "POST"])
def postME():
   data = request.get_json()
   #    data = jsonify(data)
   print(data)
   global gameThread
   # gameThread.join()


   with open("data.txt", 'w') as f:
      f.write(str(data))
   
   global time1
   time1 = os.path.getmtime('data2.txt')
   with open("data2.txt", 'w') as f:
      f.write("Modify Check File")
      print(time1)


   return data



# Send Data
@app.route("/sender", methods=["GET", "POST"])
def sendME():
   read = False
   global turnCount
   if turnCount == 0:
      time.sleep(5.0)
      turnCount = 1
      print("1st")
   else:
      print("2nd")
      time.sleep(1.5)
   # time.sleep(5.0)
   while not read:
      # exec(open('fileWatch.py').read())
      # time1 = os.path.getmtime('data2.txt')
      # print(time1)


      # if time1 != os.path.getmtime('data2.txt'):
         print(f"YERR  {time1}")
         with open("data.txt", 'r') as f:
            data = str(f.readline())
            print("YER", data)
            read = True

   # return "POLO"
   # return data
   # return json.dumps(data)
   return jsonify(data)



if __name__ == "__main__": 
   app.run(debug=True,host="0.0.0.0", port="5000")

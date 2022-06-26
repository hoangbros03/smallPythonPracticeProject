import random
import tkinter as tkinter
#from tkinter import *

#definition
#idea: make graphic, show history, show history of times roll

continueLoopSoftware = True

def returnResult(randomNumber):
   # toReturn
    for i in range(0,randomNumber,1):
        toReturn = random.randint(1,6)
    return toReturn
def printDice(result):
    if(result==1):
        print("1")
    elif(result==2):
        print("2")
    elif(result == 3):
        print("3")
    elif(result==4):
        print("4")
    elif(result==5):
        print("5")
    elif(result==6):
        print("6")
    return
def startSoftware():
    print("Welcome to dice rolling system")
    loop = True 
        # times = int(input('Type times you need to roll (normally 1 is enough - no input string!): '))
        # RollButton.configure(command=printDice(returnResult(times)))
        # result = returnResult(times)
    print("Thanks for using! Feel free to exit.")
    return 

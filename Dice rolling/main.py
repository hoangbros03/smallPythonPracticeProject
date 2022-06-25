import random
#definition
#idea: make graphic, show history, show history of times roll
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

print("Welcome to dice rolling system")
loop = True
while(loop):
    
    times = int(input('Type times you need to roll (normally 1 is enough): '))
    randomNumber = 1
    result = returnResult(randomNumber)
    printDice(result)
    stringInput ="ss"
    while(stringInput !='y'and stringInput !='n'):
        stringInput = input("Do you want to re-roll? <y/n - no UpperCase available> ")
    if(stringInput=="n"):
        loop=False
print("Thanks for using! Feel free to exit.")
    
from cgitb import text
#from curses import window
import tkinter as tk
import tkinter.ttk as ttk
from turtle import bgcolor


class Render:
    def __init__(self):
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        self.window = tk.Tk(screenName="Dice rolling system",
                            className="Dice rolling system")
        self.valueOfScreen = str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT)
        self.window.geometry(self.valueOfScreen)
        self.greeting = ttk.Label(
            text='Welcome to dice rolling system',
            background='red',
            width=SCREEN_WIDTH)
        self.rollButton = ttk.Button(text="Roll Now!", width=25)
        self.entryNumberOfRerollPerRoll = ttk.Entry(width=25)

    def packRender(self):
        self.greeting.pack()
        self.rollButton.pack()
        self.entryNumberOfRerollPerRoll.pack()
        print("Worked")

    def mainLoop(self):
        self.window.mainloop()

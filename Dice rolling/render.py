from cgitb import text
#from curses import window
import tkinter as tk
import tkinter.ttk as ttk
from turtle import bgcolor
import main as main


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
            background='red')
        self.rollButton = ttk.Button(text="Roll Now!", width=25)
        self.entryNumberOfRerollPerRoll = ttk.Entry(width=25)

        self.btn_increaseTRPR = ttk.Button(
            text="+", command=main.increaseTRPR)
        self.label_TRPR = ttk.Label(text=main.timesRerollPerRoll)
        self.label_TRPR['text'] = "uploaded"
        self.btn_decreaseTRPR = ttk.Button(
            text="-",
            command=main.decreaseTRPR,
        )

    def packRender(self):

        self.rollButton.pack()
        self.entryNumberOfRerollPerRoll.pack()
        print("Worked")

    def gridRender(self):
        self.window.rowconfigure(0, minsize=50, weight=1)
        self.window.columnconfigure([0, 1, 2], minsize=50, weight=1)
        self.greeting.grid(row=0, pady=5)
        self.btn_increaseTRPR.grid(row=1, column=0, sticky="nsew")
        self.label_TRPR.grid(row=1, column=1)
        self.label_TRPR['text'] = main.timesRerollPerRoll
        # self.btn_decreaseTRPR.configure(bg="blue")
        self.btn_decreaseTRPR.grid(row=1, column=2, sticky="nsew")
        self.greeting1 = ttk.Label(
            text='Welcome to dice rolling system',
            background='red')
        self.greeting1.grid(row=2, sticky="nsew")
        print("TRPR is to : {} ".format(main.timesRerollPerRoll))

    # def render_increaseTRPR(self):

    # def render_decreaseTRPR(self):

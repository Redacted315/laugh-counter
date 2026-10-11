import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk


def quit(event=None):
    sys.exit()

colors = {
    "primary": "#17153B",
    "secondary": "#2E236C",
    "tertiary": "#433D8B",
    "accent": "#C8AcD6"
}

BASE_DIR = Path(__file__).resolve().parent
ICON_PATH = BASE_DIR / "assets" / "smiley.png"

class Counter(tk.Tk):
    def __init__(self, player_1: str = "Player 1", player_2: str = "Player 2"):
        super().__init__()
        self.title("Laugh Counter")
        self.resizable(False, False)
        self.iconphoto(True, tk.PhotoImage(file=str(ICON_PATH)))
        self.configure(bg=colors["primary"])

        self.player1Name = player_1
        self.player1Score = 0
        self.player1Label= None
        self.player2Name = player_2
        self.player2Score = 0
        self.player2Label = None

        self.configureStyles()
        self.create_widgets()

        self.bind("w", self.player1Laugh)
        self.bind("s", self.player1UnLaugh)
        
        self.bind("<Up>", self.player2Laugh)
        self.bind("<Down>", self.player2UnLaugh)

        self.bind("<Control-r>", self.resetScores)
        self.bind("<Control-q>", quit)
        

    def resetScores(self, event=None):
        self.player1Score = 0
        self.player2Score = 0
        if isinstance(self.player1Label, ttk.Label):
            self.player1Label.config(text=self.player1Score)
        if isinstance(self.player2Label, ttk.Label):
            self.player2Label.config(text=self.player2Score)

    def create_widgets(self):
        # [ [ < 12 > ] ]
        # [    name    ]

        # player frame
        mainFrame = ttk.Frame(self, width=20, style="bg2.TFrame")

        scoreFrame = ttk.Frame(mainFrame, width=12, style="ScoreFrame.TFrame")
        lowerButton = ttk.Button(scoreFrame, text="<", width=2, style="Change.TButton", command=self.player1UnLaugh)
        scoreLabel = ttk.Label(scoreFrame, text=self.player1Score, style="Score.TLabel")
        higherButton = ttk.Button(scoreFrame, text=">", width=2, style="Change.TButton", command=self.player1Laugh)

        nameLabel = ttk.Label(mainFrame, text=self.player1Name, anchor="center", style="Name.TLabel")

        self.player1Label = scoreLabel

        lowerButton.pack(side='left', padx=15)
        scoreLabel.pack(side='left')
        higherButton.pack(side='left', padx=15)

        scoreFrame.pack(side='top', padx=10, pady=20)
        nameLabel.pack(side='top', pady=20, ipadx=15)
        mainFrame.pack(side='left', ipadx=10, ipady=10, padx=(15, 0), pady=15)
        ######### repeated for player 2 #########
        mainFrame2    = ttk.Frame(self, width=20, style="bg2.TFrame")
        scoreFrame2   = ttk.Frame(mainFrame2, width=12, style="ScoreFrame.TFrame")
        lowerButton2  = ttk.Button(scoreFrame2, text="<", width=2, style="Change.TButton", command=self.player2UnLaugh)
        scoreLabel2   = ttk.Label(scoreFrame2, text=self.player2Score, style="Score.TLabel")
        higherButton2 = ttk.Button(scoreFrame2, text=">", width=2, style="Change.TButton", command=self.player2Laugh)
        nameLabel2    = ttk.Label(mainFrame2, text=self.player2Name, anchor="center", style="Name.TLabel")
        self.player2Label = scoreLabel2
        lowerButton2.pack(side='left', padx=15)
        scoreLabel2.pack(side='left')
        higherButton2.pack(side='left', padx=15)
        scoreFrame2.pack(side='top', padx=10, pady=20)
        nameLabel2.pack(side='top', pady=20, ipadx=15)
        mainFrame2.pack(side='left', ipadx=10, ipady=10, padx=(15, 15), pady=15)

    def player1Laugh(self, event=None):
        self.player1Score += 1
        if isinstance(self.player1Label, ttk.Label):
            self.player1Label.config(text=self.player1Score)

    def player1UnLaugh(self, event=None):
        self.player1Score -= 1
        if isinstance(self.player1Label, ttk.Label):
            self.player1Label.config(text=self.player1Score)

    def player2Laugh(self, event=None):
        self.player2Score += 1
        if isinstance(self.player2Label, ttk.Label):
            self.player2Label.config(text=self.player2Score)

    def player2UnLaugh(self, event=None):
        self.player2Score -= 1
        if isinstance(self.player2Label, ttk.Label):
            self.player2Label.config(text=self.player2Score)

    def configureStyles(self):
        style = ttk.Style(self)
        style.configure(
            "bg2.TFrame",
            background=colors["secondary"],
            relief="raised",
            borderwidth=4,
        )
        style.configure(
            "Name.TLabel",
            font=("mono", 28),
            background=colors["tertiary"],
            foreground=colors["accent"],
            relief="solid",
            borderwidth=2,
            bordercolor=colors["primary"],
        )
        style.configure(
            "Score.TLabel",
            font=("mono", 32),
            background=colors["secondary"],
            foreground=colors["accent"],
            relief="none",
        )
        style.configure(
            "Change.TButton",
            font=("mono", 20, "bold"),
            background=colors["tertiary"],
            foreground=colors["primary"],
            borderwidth=2,
        )
        style.configure(
            "ScoreFrame.TFrame",
            background=colors["secondary"],
            relief="none",
            borderwidth=0,
        )

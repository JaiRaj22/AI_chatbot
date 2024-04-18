import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle

class Player(NamedTuple):
    label: str
    color: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)

class Tictactoe:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self.players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self.players)
        self.winner_combo = []
        self.current_moves = []
        self.has_winner = False
        self.winning_combos = []
        self.setup_board()
        
    def setup_board(self):
        self.current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self.winning_combos = self.combos()
        
    def combos(self):
        rows= [
            [(move.row, move.col) for move in row]
            for row in self.current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        firstdiagonal = [row[i] for i, row in enumerate(rows)]
        secondiagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [firstdiagonal, secondiagonal]
    
    def validmove(self, move):
        row, col = move.row, move.col
        movenotplayed = self.current_moves[row][col].label == ""
        no_winner = not self.has_winner
        return no_winner and movenotplayed
    
    def processmove(self, move):
        row, col = move.row, move.col
        self.current_moves[row][col] = move
        for combo in self.winning_combos:
            results = set(
                self.current_moves[n][m].label
                for n ,m in combo
            )
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self.has_winner = True
                self.winner_combo = combo
                break
            
    def winner(self):
        return self.has_winner
    
    def is_tied(self):
        no_winner = not self.has_winner
        playedMoves = (
            move.label for row in self.current_moves for move in row
        )
        return no_winner and all(playedMoves)
    
    def toggle_player(self):
        self.current_player = next(self.players)
    
class Board(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic-tac-toe")
        self._cells = {}
        self.game = game
        self.board_display()
        self.grid()
        
    def board_display(self):
        frame = tk.Frame(master=self)
        frame.pack(fill = tk.X)
        self.display = tk.Label(
            master=frame,
            text='Ready',
            font = font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def grid(self):
        gridframe = tk.Frame(master=self)
        gridframe.pack()
        for row in range(self.game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self.game.board_size):
                button = tk.Button(
                    master=gridframe,
                    text='',
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
                
    def play(self, event):
        clickedbtn = event.widget
        row, col = self._cells[clickedbtn]
        move = Move(row, col, self.game.current_player.label)
        if self.game.validmove(move):
            self.updatebutton(clickedbtn)
            self.game.processmove(move)
            if self.game.is_tied():
                self.updatedisplay(msg="Tied game", color="red")
            elif self.game.winner():
                self.highlightcells()
                msg = f'Player "{self.game.current_player.label}" won!'
                color = self.game.current_player.color
                self.updatedisplay(msg, color)
            else:
                self.game.toggle_player()
                msg = f"{self.game.current_player.label}'s turn"
                self.updatedisplay(msg)
                
    def updatebutton(self, clickedbtn):
        clickedbtn.config(text=self.game.current_player.label)
        clickedbtn.config(fg=self.game.current_player.color)
        
    def updatedisplay(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color
        
    def highlightcells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self.game.winner_combo:
                button.config(highlightbackground="red")
        
def main():
    gaame = Tictactoe()
    bord = Board(gaame)
    bord.mainloop()

if __name__ == "__main__":
    main()
    
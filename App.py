import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        schachbrett = ChessBoard()
        schachbrett.pack(side="left")


class ChessBoard(ttk.Frame):
    def __init__(self):
        super().__init__()

        self.squares = [[None] * 8] * 8  # [0][0] is square A1 -> [7][7] = H8
        self.colors = ("black", "white")
        self.setup_board()

    @classmethod
    def _from_rgb(cls, rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb

    def setup_board(self):
        for i in range(8):
            for j in range(8):
                self.squares[i][j] = tk.Button(self, background=self.colors[(i+j) % 2], width=10, height=5)
                self.squares[i][j].grid(row=i, column=j)


if __name__ == "__main__":
    app = App()
    app.mainloop()

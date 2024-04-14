import tkinter as tk
from tkinter import messagebox


class Board:
    def __init__(self) -> None:
        self.xIndexes: list[tuple] = []
        self.oIndexes: list[tuple] = []
        self.board: list[str] = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.turn = 'x'
    
    def getSpot(self, x: int, y: int) -> str:
        return self.board[x][y]
    
    def setSpot(self, s, x: int, y: int, data: str = ' ') -> None:
        if self.getSpot(x, y) != ' ' and data != ' ':
            print('Nope')
            return
        if data == 'x':
            if len(self.xIndexes) == 3:
                ind = self.xIndexes.pop(0)
                self.xIndexes.append((x, y))
                self.setSpot(None, ind[0], ind[1])
                s.buttons[ind[0]][ind[1]]['text'] = ""
            else:
                self.xIndexes.append((x, y))
        elif data == 'o':
            if len(self.oIndexes) == 3:
                ind = self.oIndexes.pop(0)
                self.oIndexes.append((x, y))
                self.setSpot(None, ind[0], ind[1])
                s.buttons[ind[0]][ind[1]]['text'] = ""
            else:
                self.oIndexes.append((x, y))
        self.board[x][y] = data
        if self.checkWin('x'):
            s.buttons[x][y]['text'] = 'x'
            for i in range(len(s.buttons)):
                for j in range(len(s.buttons[i])):
                    s.buttons[i][j]['state'] = 'disabled'
            messagebox.showinfo(message='x Won')
            exit()
        if self.checkWin('o'):
            s.buttons[x][y]['text'] = 'o'
            for i in range(len(s.buttons)):
                for j in range(len(s.buttons[i])):
                    s.buttons[i][j]['state'] = 'disabled'
            messagebox.showinfo(message='o Won')
            exit()

    def userTurn(self, s, x: int, y: int) -> str:
        if self.turn == 'x':
            self.setSpot(s, x, y, 'x')
            self.turn = 'o'
            return 'x'
        self.setSpot(s, x, y, 'o')
        self.turn = 'x'
        return 'o'

    def checkWin(self, player: str) -> bool:
        for row in self.board:
            if all([spot == player for spot in row]):
                return True

        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2-i] == player for i in range(3)]):
            return True

        return False


class TicTacToeBoard:
    def __init__(self, master) -> None:
        self.b = Board()
        self.master = master
        self.master.title("Tic Tac Toe")

        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text="", font=('Arial', 30), width=5, height=2,
                                               command=lambda row=i, col=j: self.button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def button_click(self, row, col) -> None:
        val = self.b.userTurn(self, row, col)
        self.buttons[row][col]['text'] = val

def main():
    root = tk.Tk()
    app = TicTacToeBoard(root)
    root.mainloop()

if __name__ == "__main__":
    main()

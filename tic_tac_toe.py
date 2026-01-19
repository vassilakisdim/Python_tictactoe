import random
import os
import tkinter as tk, tkinter.ttk as ttk
from tkinter import font
from tkinter import Tk, Frame, Button
from functools import partial
from tkinter.filedialog import askopenfilename
from tkinter import *
import threading

prefs = [0, 2, 6, 8]
board = [" "] * 9

ch = "default"
zzz = ""




#GUI--------------------------------------#

########DEBUG_LINE############
#board[0] = "X"  #Keep disabled
######END_OF_DEBUG_LINE#######
base = Tk()
base.geometry("300x300")
a = Label(base, text="Tic Tac Toe Game")
g = Label(base, text="Game Ongoing")
cfont = tk.font.Font(family='Helvetica', size=30, weight='bold')
a.pack()


v = tk.StringVar()

def end_result():
    T = Text(base)
end_result()

def reset():
    board[0]=" "
    board[1]=" "
    board[2]=" "
    board[3]=" "
    board[4]=" "
    board[5]=" "
    board[6]=" "
    board[7]=" "
    board[8]=" "
    g.config(text='Game Ongoing')
    g.pack()
    elements()


def btn_click(i):
    global ch
    ch = i
    player_move()
    if check_winner(board, "X"):
        g.config(text='Player won')
        g.pack()
    if check_draw(board):
        g.config(text="It's a draw")
        g.pack()
    ai_move()
    a_Board = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]]
    Tk.update(base)
    Tk.update_idletasks(base)
    elements()
    if check_draw(board):
        g.config(text="It's a draw")
        g.pack()
    if check_winner(board, 0):
        g.config(text='AI won')
        g.pack()

# Layout for Board
btns_frame = Frame(base)
btns_frame.pack()
def elements():
    a_Board = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]]
    for row in range(len(a_Board)):
        for col in range(len(a_Board[row])):
            i = a_Board[row][col]
            param = str(row * 3 + col)
            b = Button(btns_frame, text=str(i), height=1, width=2, font=cfont, command= partial(btn_click, param))
            b.pack
            b.grid(row=row + 1, column=col)
elements()
g.pack()

res = Button(base, text="Reset", command= reset)
res.pack()
#End_of_GUI

#DEFINITIONS


def player_move():
    while True:
        if check_draw(board):
            g.config(text="It's a draw")
            g.pack()
            return
        elif check_winner(board, "X"):
            g.config(text='Player Won')
            g.pack()
            elements()
            return
        elif check_winner(board, 0):
            g.config(text='AI won')
            g.pack()
            elements()
            return
        else:
            choice = ch
            #print(type(choice))        #exclusively for debug purposes
            if str.isdigit(choice):
                choice = int(choice)
                if 0 <= choice <= 8 and board[choice] == " ":
                    board[choice] = "X"
                    zzz = True
                    break
                else:
                    pass
            else:
                pass
        a_Board = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]]
        Tk.update(base)
    Tk.update_idletasks(base)
    elements()

def ai_move():
    free = [i for i , x in enumerate(board) if x==" "]
    #try to win
    if check_draw(board):
        g.config(text="It's a draw")
        g.pack()
        elements()
        return
    if check_winner(board, "X"):
        g.config(text='Player Won')
        g.pack()
        elements()
        return
    elif check_winner(board, 0):
        g.config(text='AI won')
        g.pack()
        elements()
        return
    for i in free:
        board[i]=0
        if check_winner(board, 0):
            return
        else:
            board[i] = " "
    #block_peasant
    for y in free:
        board[y] = "X"
        if check_winner(board, "X"):
            board[y] = 0
            return
        board[y] = " "
    #desperate_block_attempt
    for i in free:
        if 4 in free:
            board[4] = 0
            return
        elif y in free:
            pick = random.choice(prefs)
            if board[pick] == " ":
                board[pick] = 0
                return
        else:
            pass
    move = random.choice(free)
    board[move] = 0
    a_Board = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]]
    Tk.update(base)
    Tk.update_idletasks(base)
    elements()


def check_row(b,p):
    row_start = [0,3,6]
    for i in range(3):
        if b[row_start[0]] == b[row_start[0]+1] == b[row_start[0]+2] == p:
            return True
        else:
            row_start.pop(0)

def check_col(b,p):
    row_start = [0,1,2]
    for i in range(3):
        if b[row_start[0]] == b[row_start[0]+3] == b[row_start[0]+6] == p:
            return True
        else:
            row_start.pop(0)

def check_diagon(b,p):
    if b[0] == b[4] == b[8] ==  p:
        return True
    if b[2] == b[4] == b[6] ==  p:
        return True

def check_winner(b,p):
    if check_row(b,p):
        return True
    if check_col(b,p):
        return True
    if check_diagon(b,p):
        return True
    
def check_draw(b):
    if [i for i, x in enumerate(b) if x == " "] == []:
        return True
    else:
        return False

#END_OF_DEFINITIONS


turn = 0

playerData = {
    0: {"symbol": 0, "name": "AI"},
    1: {"symbol": "X", "name": "player"},

}

while True:
    Tk.update(base)
    if zzz == True:
        if (turn % 2) == 1:
            player_move()
        else:
            ai_move()
        if check_winner(board, playerData[turn %2]["symbol"]):
            g.config(text=(playerData[turn %2]["name"], " won"))
            g.pack()
            break
        if check_draw(board):
            g.config(text="It's a draw")
            g.pack()
            break
        a_Board = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]]
        Tk.update(base)
        Tk.update_idletasks(base)
        elements()
        zzz = ""
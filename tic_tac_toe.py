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

#DEFINITIONS

#GUI--------------------------------------#

########DEBUG_LINE############
#board[0] = "X"  #Keep disabled
######END_OF_DEBUG_LINE#######
base = Tk()
base.geometry("300x200")
a = Label(base, text="Tic Tac Toe Game")
a.pack()


v = tk.StringVar()

# def setText(word):
#     v.set(word)

# def clear_text():
#    sel.delete(0, END)


def btn_click(i):
    global ch
    ch = i
    player_move()
    if check_winner(board, "X"):
        print("Player won")
        a = Label(base, text="Player Won")
    if check_draw(board):
        print("It's a draw")
        a = Label(base, text="It's a draw")
    print(" ")
    ai_move()
    a_Board = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]]
    Tk.update(base)
    Tk.update_idletasks(base)
    elements()
    #base.mainloop()
    if check_draw(board):
        print("It's a draw")
        a = Label(base, text="It's a draw")
    #os.system('cls')
    if check_winner(board, 0):
        print("AI won")
        a = Label(base, text="AI won")

# Layout for Board
btns_frame = Frame(base)
btns_frame.pack()
def elements():
    a_Board = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]]
    for row in range(len(a_Board)):
        for col in range(len(a_Board[row])):
            i = a_Board[row][col]
            param = str(row * 3 + col)
            b = Button(btns_frame, text=str(i), command= partial(btn_click, param))
            b.pack
            b.grid(row=row + 1, column=col)
elements()

# sel = (ttk.Entry(base, textvariable=""))
# sel.pack()
# opt = str(sel)




# def submit():
#     global ch
#     global zzz
#     ch=sel.get()
#     print("Player Chose : " + ch)
#     print(type(ch))
#     zzz = True
#     sel.set("")
#     v.set("")
#     clear_text()
#     #player_move()

# def submitandclear():
#     submit()
#     clear_text()
    
# b = ttk.Button(base, text="Submit", command=submitandclear)
# b.pack()
# #End_of_GUI


def show(b):
    print(f"{b[0]}|{b[1]}|{b[2]}")
    print("-+-+-")
    print(f"{b[3]}|{b[4]}|{b[5]}")
    print("-+-+-")
    print(f"{b[6]}|{b[7]}|{b[8]}")

def player_move():
    while True:
        if check_draw(board):
            print("It's a draw")
            a = Label(base, text="It's a draw")
            return
        elif check_winner(board, "X"):
            print("Player won")
            a = Label(base, text="Player Won")
            elements()
            return
        elif check_winner(board, 0):
            print("AI won")
            a = Label(base, text="AI won")
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
                    print("taken")
            else:
                print ("This is not a valid option, try again")
        a_Board = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]]
        Tk.update(base)
    Tk.update_idletasks(base)
    elements()
    #sel.set("")
    show(board)

def ai_move():
    free = [i for i , x in enumerate(board) if x==" "]
    #try to win
    if check_draw(board):
        print("It's a draw")
        a = Label(base, text="It's a draw")
        elements()
        return
    if check_winner(board, "X"):
        print("Player won")
        a = Label(base, text="Player Won")
        elements()
        return
    elif check_winner(board, 0):
        print("AI won")
        a = Label(base, text="AI won")
        elements()
        return
    for i in free:
        board[i]=0
        if check_winner(board, 0):
            show(board)
            return
        else:
            board[i] = " "
    #block_peasant
    for y in free:
        board[y] = "X"
        if check_winner(board, "X"):
            board[y] = 0
            show(board)
            return
        board[y] = " "
        #pass
    #desperate_block_attempt
    for i in free:
        if 4 in free:
            board[4] = 0
            show(board)
            return
        elif y in free:
            pick = random.choice(prefs)
            if board[pick] == " ":
                board[pick] = 0
                show(board)
                return
        else:
            pass
    move = random.choice(free)
    board[move] = 0
    show(board)
    a_Board = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]]
    Tk.update(base)
    Tk.update_idletasks(base)
    elements()




def check_winner(b,p):
    if b[0] == b[1] == b[2] ==  p:
        return True
    if b[3] == b[4] == b[5] ==  p:
        return True
    if b[6] == b[7] == b[8] ==  p:
        return True
    if b[0] == b[3] == b[6] ==  p:
        return True
    if b[1] == b[4] == b[7] ==  p:
        return True
    if b[2] == b[5] == b[8] ==  p:
        return True
    if b[0] == b[4] == b[8] ==  p:
        return True
    if b[2] == b[4] == b[6] ==  p:
        return True
#if len([i for i, x in enumerate(b) if x == " "]) == 0:
def check_draw(b):
    if [i for i, x in enumerate(b) if x == " "] == []:
        return True
    else:
        return False

#END_OF_DEFINITIONS


show(board)
# for i in range (2):
while True:
    Tk.update(base)
    if zzz == True:
        print(zzz)
        player_move()
        if check_winner(board, "X"):
            print("Player won")
            a = Label(base, text="Player Won")
            break
        if check_draw(board):
            print("It's a draw")
            a = Label(base, text="It's a draw")
            break
        print(" ")
        ai_move()
        a_Board = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]]]
        Tk.update(base)
        Tk.update_idletasks(base)
        elements()
        #base.mainloop()
        if check_draw(board):
            print("It's a draw")
            a = Label(base, text="It's a draw")
            break
        #os.system('cls')
        if check_winner(board, 0):
            print("AI won")
            a = Label(base, text="AI won")
            break
        zzz = ""
    



base.mainloop()




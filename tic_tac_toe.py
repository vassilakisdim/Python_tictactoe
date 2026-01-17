import random
import os

prefs = [0, 2, 6, 8]
board = [" "] * 9

def show(b):
    print(f"{b[0]}|{b[1]}|{b[2]}")
    print("-+-+-")
    print(f"{b[3]}|{b[4]}|{b[5]}")
    print("-+-+-")
    print(f"{b[6]}|{b[7]}|{b[8]}")

def player_move():
    while True:
        choice = int(input("number: "))
        if 0 <= choice <= 8 and board[choice] == " ":
            board[choice] = "X"
            break
        else:
            print("taken")
    show(board)

def ai_move():
    free = [i for i , x in enumerate(board) if x==" "]
    #try to win
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

show(board)
# for i in range (2):
while True:
    player_move()
    if check_winner(board, "X"):
        print("Player won")
        break
    if check_draw(board):
        print("It's a draw")
        break
    print(" ")
    ai_move()
    if check_draw(board):
        print("It's a draw")
        break
    #os.system('cls')
    if check_winner(board, 0):
        print("AI won")
        break



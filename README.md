# Python_tictactoe
A project aimed to create a fully playable Tic Tac Toe game usig python.
Currently there is no GUI, so the board is displaayed using text in this board: (remind me to change this when I make a GUI build)

0|1|2
-+-+-
3|4|5
-+-+-
6|7|8

# A general explaanation of the bot's code

The bot has this priority when playing
 - Complete a row of 3
 - Block the player if he/she is ready to complete a row
 - Pick the center square (4)
 - Pick one of the edges
 - Pick one of the following squares: [1, 3, 5, 7]

Obviously, instructions like "Pick the center square" will get skipped if the squares are taken, and the bot will pick a move lower in the priority list

# Notes

- Future builds will mainly focus on the development of  GUI and\or bug fixes, since I think the bot is good enough
- In case of a suggestion, please open a request :)

def drawboard(board):
    print('   |   |')
    print(' ' + str(board[7]) + ' | ' +str( board[8]) + ' | ' + str(board[9]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(board[4]) + ' | ' + str(board[5]) + ' | ' + str(board[6]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3]))
    print('   |   |')
def draw(board):
    print(board[7], board[8], board[9])
    print(board[4], board[5], board[6])
    print(board[1], board[2], board[3])
    print()
def t(board):
    while True:
            try:
                    x = int(input())
                    if x in board:
                            return x
                    else:
                            print("\nSpace already taken. Try again")
            except ValueError:
                    print("\nThat's not a number. enter a space 1-9")
def GO(win,board):
    for x, o, b in win:
            if board[x] == board[o] == board[b]:
                    print("Player {0} wins!\n".format(board[x]))
                    print("Congratulations! You've won :v\n")
                    return True
    if 9 == sum((pos == 'X' or pos == 'O') for pos in board):
            print("It's a tie\n")
            return True
def tic_tac_toe():
    board = [None] + list(range(1, 10))
    win = [(1, 2, 3),(4, 5, 6),(7, 8, 9),(1, 4, 7),(2, 5, 8),(3, 6, 9),(1, 5, 9),(3, 5, 7),]
    for player in 'XO' * 9:
            drawboard(board)
            if GO(win,board):
                    break
            print("Player {0}".format(player))
            board[t(board)] = player
            print()
def main():
    while True:
            tic_tac_toe()
            if input("Play again (y/n)\n") != "y":
                    break
main()
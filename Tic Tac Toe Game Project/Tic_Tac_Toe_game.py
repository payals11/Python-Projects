"""
   TIC TAC TOE Game

Created on August 12, 2020
@author: Payal Shinde

"""

global player1_marker, player2_marker


def display_board(board: "list"):
    print("Here is the current board..")
    print('     ' + '|' + '     ' + '|' + '     ')
    print('  ' + board[7] + '  ' + '|' + '  ' + board[8] + '  ' + '|' + '  ' + board[9] + '  ')
    print('     ' + '|' + '     ' + '|' + '     ')
    print('-----------------')
    print('     ' + '|' + '     ' + '|' + '     ')
    print('  ' + board[4] + '  ' + '|' + '  ' + board[5] + '  ' + '|' + '  ' + board[6] + '  ')
    print('     ' + '|' + '     ' + '|' + '     ')
    print('-----------------')
    print('     ' + '|' + '     ' + '|' + '     ')
    print('  ' + board[1] + '  ' + '|' + '  ' + board[2] + '  ' + '|' + '  ' + board[3] + '  ')
    print('     ' + '|' + '     ' + '|' + '     ')
    print()


def game_result(resultboard: "list", num: "int"):
    if ((resultboard[7] == resultboard[8] == resultboard[9] == player1_marker) or
            (resultboard[7] == resultboard[5] == resultboard[3] == player1_marker) or
            (resultboard[9] == resultboard[5] == resultboard[1] == player1_marker) or
            (resultboard[7] == resultboard[4] == resultboard[1] == player1_marker) or
            (resultboard[2] == resultboard[5] == resultboard[8] == player1_marker) or
            (resultboard[3] == resultboard[6] == resultboard[9] == player1_marker) or
            (resultboard[4] == resultboard[5] == resultboard[6] == player1_marker) or
            (resultboard[1] == resultboard[2] == resultboard[3] == player1_marker)):
        print()
        print()
        print(f"Congratulations! Player1 having marker '{player1_marker}' has won the game!!!!!\n")
        exit()
    elif ((resultboard[7] == resultboard[8] == resultboard[9] == player2_marker) or
          (resultboard[7] == resultboard[5] == resultboard[3] == player2_marker) or
          (resultboard[9] == resultboard[5] == resultboard[1] == player2_marker) or
          (resultboard[7] == resultboard[4] == resultboard[1] == player2_marker) or
          (resultboard[2] == resultboard[5] == resultboard[8] == player2_marker) or
          (resultboard[3] == resultboard[6] == resultboard[9] == player2_marker) or
          (resultboard[4] == resultboard[5] == resultboard[6] == player2_marker) or
          (resultboard[1] == resultboard[2] == resultboard[3] == player2_marker)):
        print()
        print()
        print(f"Congratulations! Player2 having marker '{player2_marker}' has won the game!!!!!\n")
        exit()
    elif num == 9:
        print()
        print()
        print("The game is tie!!!!!")
        exit()


def test_board(board: "list", var: "int" = None, num: "int" = None) -> "list":
    if var is not None and num is not None:
        if num % 2 != 0:
            board[var] = player1_marker
        else:
            board[var] = player2_marker
    display_board(board)
    return board


def player_input() -> tuple[str, str]:
    player1 = str()
    player2 = str()
    marker = False

    while not marker:
        player1 = str(input("Player1 : Enter which marker you want to select 'X or 0':"))
        if player1.strip() not in ('X', 'x', '0'):
            print("Sorry, you have entered incorrect marker!!\n")
        else:
            if player1.strip() in ('X', 'x'):
                player2 = '0'
            marker = True
    return player1, player2


def select_position(num: "int"):
    print("\nBoard number positions will be like below:")
    print('   ' + '|' + '   ' + '|' + '   ')
    print(' 7 ' + '|' + ' 8 ' + '|' + ' 9 ')
    print('   ' + '|' + '   ' + '|' + '   ')
    print('---------')
    print('   ' + '|' + '   ' + '|' + '   ')
    print(' 4 ' + '|' + ' 5 ' + '|' + ' 6 ')
    print('   ' + '|' + '   ' + '|' + '   ')
    print('---------')
    print('   ' + '|' + '   ' + '|' + '   ')
    print(' 1 ' + '|' + ' 2 ' + '|' + ' 3 ')
    print('   ' + '|' + '   ' + '|' + '   ')
    print()

    player = str()
    if num % 2 == 0:
        player = 'Player2'
    else:
        player = 'Player1'

    pos = str()
    pos_entered = False
    while not pos_entered:
        pos = input(f"{player}, Enter position in number range [1-9]:")
        if pos.strip().isdigit():
            pos = int(pos)
            if pos in range(1, 10):
                pos_entered = True
            else:
                print("Sorry, you have entered out of range input!!\n")
                pos_entered = False
        else:
            print("Sorry, entered input is not digit!!")
            pos_entered = False
    return pos


if __name__ == '__main__':
    print("#########################################################################")
    print()
    print("                Welcome to TIC TAC TOE Game                              ")
    print()
    print("#########################################################################")
    print()
    player1_marker, player2_marker = player_input()
    print("Player1 marker = " + player1_marker)
    print("Player2 marker = " + player2_marker)
    print()
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    board = test_board(board)
    cnt = 1
    game_on = 'Y'

    while game_on == 'Y' or cnt == 9:
        pos = select_position(cnt)
        result_board = test_board(board, pos, cnt)
        cnt += 1
        if cnt >= 5:
            game_result(result_board, cnt)
        choice = False

        while not choice:
            choice = input("Do you want to continue playing 'Y or N':")
            if choice.strip() not in ('Y', 'y', 'n', 'N'):
                print("Sorry, you have entered invalid input!!\n")
                choice = False
            else:
                if choice in ('n','N'):
                    exit()
                else:
                    choice = True

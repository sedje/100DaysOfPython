import re
import os


def print_board(score=None):
    positions = [0, 2, 6, 10]
    board = [list('  1   2   3'),
             list('1   |   |   '),
             list('2   |   |   '),
             list('3   |   |   ')]
    if score:
        for position, player in score.items():
            position = position.split(',')
            board[int(position[0])][positions[int(position[1])]] = player
    for row in board:
        print(''.join(row))


def check_win(score):

    winner = None
    for row in range(1, 3):

        # Check the horizontal values, if they match, declare the winner
        try:
            if score[f"{row},1"] == score[f"{row},2"] == score[f"{row},3"]:
                winner = score[f"{row},1"]
        except KeyError:
            pass

        # Check the vertical values, if they match, declare the winner
        try:
            if score[f"1,{row}"] == score[f"2,{row}"] == score[f"3,{row}"]:
                winner = score[f"1,{row}"]
        except KeyError:
            pass

    # Check the Diagonal values, if they match, declare the winner
    try:
        if (score["1,1"] == score["2,2"] == score["3,3"]) or (score["3,1"] == score["2,2"] == score["1,3"]):
            winner = score["2,2"]
    except KeyError:
        pass

    if winner:
        print(f"Player {winner} has won!")
        print("Thanks for playing")
        return True
    elif len(score) == 9:
        print("The game is a draw")
        return True

    return False


def main():
    game_over = False
    player = "O"
    score = {}
    message = 'Welcome to tic-tac-toe'
    print(message)
    print_board(score)
    while not game_over:
        value = input("Please provide your desired position, i.e. 1,1: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if re.match('^[1-3],[1-3]$', value):
            if value in score:
                message = "That position is already taken"
            else:
                score[value] = player
                message = f"Player {player} took position {value}"
                print_board(score)
                if player == "O":
                    player = "X"
                else:
                    player = "O"
        else:
            message = "Invalid input"
        print(message)
        game_over = check_win(score)

    if input("Want to play again? (Y/N): ").upper() == "Y":
        os.system('cls' if os.name == 'nt' else 'clear')
        main()


if __name__ == '__main__':
    main()

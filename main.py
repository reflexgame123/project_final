print("welcome!!!")

def print_board(board):
    print("/n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("/n")

def check_win(board, player):
    for i in range(3):
        if all ([cell == player for cell in board[i]]):
            return True
    if all([board[j][i] == player for j in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def check_u_win(board, player):
    return (
        board[1][0] == player and
        board[1][2] == player and
        board[2][1] == player
    )

def is_draw(board):
    return all([cell != " " for row in board for cell in row])

def get_move(player_name, board):
    while True:
        try:
            move = input(f"{player_name}, введи хід (рядок і стовпець, напр. 1 2): ").strip()
            row, col = map(int, move.split())
            if board[row][col] != " ":
                print("Ця клітинка вже зайнята. Спробуй ще")
            else:
                return row, col
        except (ValueError, IndexError):
            print("Некоректне введення. від 0 до 2 через пробіл.")

def main():
    print("Ласкаво просимо!")

    code = input("натисніть enter щоб почати.")
    u_mode = (code == "1111")
    if u_mode:
        print("Спецрежим активовано!")

    player1 = input("ім'я гравця 1 (грає Х)")
    player2 = input("м'я гравця 2(грає O )")

    board = [[" " for _ in range (3)] for _ in range(3)]
    current_player = "X"
    player_name = {"X": player1, "O": player2 }

    print_board(board)

    while True:
        row, col = get_move(player_name[current_player], board)
        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Переміг {player_name[current_player]}!")
            break
        if u_mode and check_u_win(board, current_player):
            print(f"{player_name[current_player]} виграв(ла) (способом U)")
            break
        if is_draw(board):
            print("Нічия!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
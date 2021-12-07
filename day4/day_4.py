number_sequece = [int(n) for n in open('day_4_numbers').readline().split(',')]
boards_rows = [
    [int(el) for el in line.split()]
    for line in open('day_4').readlines() if line != '\n'
]
boards = [boards_rows[i:i+5] for i in range(0, len(boards_rows), 5)]


def check_row(row, numbers):
    return set(row).issubset(set(numbers))


def check_column(board, c, numbers):
    return check_row([board[i][c] for i in range(5)], numbers)


def check_board(board, numbers):
    for row in board:
        if check_row(row, numbers):
            return True

    for column in range(5):
        if check_column(board, column, numbers):
            return True


def get_winning_board_and_number(last_wins=False):
    numbers = number_sequece[:4]
    won_boards = set()
    for number in number_sequece:
        numbers.append(number)
        for i, board in enumerate(boards):
            if check_board(board, numbers):
                if last_wins:
                    won_boards.add(i)
                    if len(won_boards) == len(boards):
                        return board, numbers
                    continue
                return board, numbers


def calc_score(board, numbers):
    board_sum = sum({n for row in board for n in row} - set(numbers))
    return board_sum * numbers[-1]


if __name__ == '__main__':
    # values = test_values
    # board, day_4_numbers = get_winning_board_and_number()

    # part 1
    board, numbers = get_winning_board_and_number(last_wins=False)
    print(calc_score(board, numbers))

    # part 2
    board, numbers = get_winning_board_and_number(last_wins=True)
    print(calc_score(board, numbers))

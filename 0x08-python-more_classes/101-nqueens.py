#!/usr/bin/python3
import sys


def init_board(n):
    """construct for placing N non-attacking queens on an N×N chessboard."""
    b = []
    [b.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in b]
    return (b)


def board_deepcopy(b):
    """This method return chessboard."""
    if isinstance(b, list):
        return list(map(board_deepcopy, b))
    return (b)


def get_solution(b):
    """This method return list copy of a solved chessboard."""
    solv = []
    for r in range(len(b)):
        for c in range(len(b)):
            if b[r][c] == "Q":
                solv.append([r, c])
                break
    return (solv)


def xout(board, row, col):
    """This out all spots diagonally down to the left

    Args:
        board (_type_): define board
        row (_type_): define row of chessebord
        col (_type_): define colum of chessebord
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """THis define recursive solution of chesseboard

    Args:
        board (_type_): define board
        row (_type_): define row
        queens (_type_): define queens
        solutions (_type_): define recursive solution

    Returns:
        solutions: solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)

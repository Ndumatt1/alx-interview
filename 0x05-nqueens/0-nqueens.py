#!/usr/bin/python3
""" N Queens module. """
import sys


def print_board(board):
    """ Print the board. """
    # Create a matrix with the indexes of the board.
    matrix = []
    # Iterate through the board.
    for i in range(len(board)):
        # Append the index and the column of the board.
        matrix.append([i, board[i][1]])
    # Print the matrix.
    print(matrix)


def backtrack(i, n, col, pos_diag, neg_diag):
    """ Backtracking function. """
    # Iterate through the columns.
    for j in range(n):
        # Check if j is not in col and i + j is not in pos_diag
        # and i - j is not in neg_diag.
        if j not in col and i + j not in pos_diag and i - j not in neg_diag:
            # Add j to col set
            col.add(j)
            # Add i + j to pos_diag set
            pos_diag.add(i + j)
            # Add i - j to neg_diag set
            neg_diag.add(i - j)
            # Append [i, j] to board.
            board.append([i, j])
            # Check if i is not n - 1 (last row).
            if i != n - 1:
                # Call backtrack function with i + 1.
                # This will move to the next row.
                backtrack(i + 1, n, col, pos_diag, neg_diag)
            else:
                # If i is n - 1 (last row), print the board.
                print_board(board)
            # If it reaches this point, that means that the board is not
            # complete, so remove the last item of the board.
            board.remove([i, j])
            # Remove j from col set
            col.remove(j)
            # Remove i + j from pos_diag set
            pos_diag.remove(i + j)
            # Remove i - j from neg_diag set
            neg_diag.remove(i - j)


# Check if the user input is one number.
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Get the size of the board.
n = sys.argv[1]

# Check if the user input is a number.
try:
    n = int(n)
except ValueError:
    print("N must be a number")
    exit(1)

# Check if the user input is at least 4.
if n < 4:
    print("N must be at least 4")
    exit(1)

# Define the board and the sets.
col = set()
pos_diag = set()
neg_diag = set()
board = []

backtrack(0, n, col, pos_diag, neg_diag)

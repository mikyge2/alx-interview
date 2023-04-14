#!/usr/bin/python3
"""program that solves the N queens problem."""
from sys import argv, exit


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

val_n = argv[1]

try:
    val_n = int(val_n)
except ValueError:
    print("N must be a number")
    exit(1)

if val_n < 4:
    print("N must be at least 4")
    exit(1)

solution = []


def nqueens(row, val_n, solution):
    """The program should print any possible solution"""
    if (row == val_n):
        print(solution)
    else:
        for col in range(val_n):
            position = [row, col]
            if validposition(solution, position):
                solution.append(position)
                nqueens(row + 1, val_n, solution)
                solution.remove(position)


def validposition(solution, position):
    """validate horizontal and diagonal position of queens"""
    for queen in solution:
        if queen[1] == position[1]:
            return False
        # descending diagonal
        if (queen[0] - queen[1]) == (position[0] - position[1]):
            return False
        # ascending diagonal
        if (queen[0] + queen[1]) == (position[0] + position[1]):
            return False
    return True


nqueens(0, val_n, solution)

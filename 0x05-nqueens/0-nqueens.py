#!/usr/bin/python3
"""N queens solution finder module."""

import sys


def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    if pos0[1] == pos1[1] or abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]):
        return True
    return False


def group_exists(group, solutions):
    """Checks if a group exists in the list of solutions.

    Args:
        group (list): A group of possible positions.
        solutions (list): The list of solutions.

    Returns:
        bool: True if the group exists, False otherwise.
    """
    for stn in solutions:
        if sorted(stn) == sorted(group):  # Compare sorted groups for unique solutions
            return True
    return False


def build_solution(row, group, n, pos, solutions):
    """Builds a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list): The current list of valid positions.
        n (int): The size of the chessboard.
        pos (list): The list of possible positions.
        solutions (list): The list to store the solutions.
    """
    if row == n:
        if not group_exists(group, solutions):
            solutions.append(group.copy())
    else:
        for col in range(n):
            current_pos = [row, col]
            if all(not is_attacking(current_pos, other_pos) for other_pos in group):
                group.append(current_pos)
                build_solution(row + 1, group, n, pos, solutions)
                group.pop()


def get_solutions(n):
    """Gets the solutions for the given chessboard size.
    
    Args:
        n (int): The size of the chessboard.
    """
    solutions = []
    pos = [[i // n, i % n] for i in range(n * n)]
    build_solution(0, [], n, pos, solutions)
    return solutions


def main():
    """Main function to execute the N queens problem."""
    n = get_input()
    solutions = get_solutions(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

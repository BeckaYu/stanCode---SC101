"""
File: boggle.py
Name: Rebecca
----------------------------------------
This program simulates the classic Boggle game.
Users are prompted to input a grid of 16 letters (4x4).
The program then identifies and displays all possible words formed from the grid,
adhering to Boggle's rules.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    Simulates a Boggle game. Users input a 4x4 grid of letters,
    and the program finds all valid words according to Boggle rules.
    Prints the total number of words found and the execution time.
    """
    start = time.time()
    ####################
    ans = []
    word_lst = read_dictionary()
    board = create_board()
    if board is None:   # If user enter invalid input
        print(f"Illegal input")
    else:
        # Starting by each letter on the board
        for x in range(1, 5):
            for y in range(1, 5):
                find_words(board, word_lst, '', ans, x, y)
    print(f'There are {len(ans)} words in total.')
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(board, word_lst, partial, ans, x, y):
    """
    Recursively searches for valid Boggle words starting from a given cell.
    Marks cells as visited during search and backtracks after exploration.
    :param board: dict, The game board with letter positions and visit status.
    :param word_lst: list, List of valid words for reference.
    :param partial: str, Current word being formed.
    :param ans: list, Accumulator for valid words found.
    :param x, y : int, Current cell coordinates.
    """
    # Ensure the search is within the board and only search for the letter has not been used
    if not (1 <= x <= 4 and 1 <= y <= 4) or board[(x, y)][1]:
        return

    board[(x, y)][1] = True    # Mark the word as been used
    partial += board[(x, y)][0]    # Adding the valid letter into the answer

    if has_prefix(partial, word_lst):   # Early stop the search if there is no such prefix in the dictionary
        if len(partial) >= 4 and partial in word_lst and partial not in ans:
            print(f'Found: {partial}')
            ans.append(partial)

        # Check each direction besides the targeted letters
        for (dx, dy) in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= 4 and 1 <= ny <= 4:
                find_words(board, word_lst, partial, ans, nx, ny)

    board[(x, y)][1] = False  # Reset the visited status
    partial = partial[:-1]   # Backtrack the partial string after exploring all adjacent cells


def create_board():
    """
    Generates the game board based on user input. Expects 4 lines of letters.
    :return: dictionary, a dictionary mapping cell coordinates to letters and visit status.
    """
    board = {}
    for row in range(4):
        letters_raw = input(f"{row + 1} row of letters: ")
        if len(letters_raw) != 7:
            return None
        else:
            letters = letters_raw.lower().split(" ")
            for letter in letters:
                if not letter.isalpha():
                    return None
                else:
                    for col in range(4):
                        board[(row + 1, col + 1)] = [letters[col], False]
    return board


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    word_lst = []
    with open(FILE, 'r') as f:
        for line in f:
            word_lst.append(line.split("\n")[0])
    return word_lst

def has_prefix(sub_s, word_lst):
    """
     Checks if any word in the dictionary starts with the given substring.
    :param sub_s: str, A substring that is constructed by neighboring letters on a 4x4 square grid
    :param word_lst: list, A list saving all valid words in the English dictionary
    :return: bool, If there is any words with prefix stored in sub_s
    """
    for word in word_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

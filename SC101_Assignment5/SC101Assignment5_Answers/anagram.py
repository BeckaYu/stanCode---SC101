"""
File: anagram.py
Name: Rebecca
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    Main function to run the anagram generator. It prompts the user to input a word and
    displays all its anagrams, measuring the time taken to find them.
    The program terminates when the user inputs the EXIT constant.
    """
    ####################
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')

    while True:
        # Prompt user for a word and measure anagram finding time
        s = input(f"Find anagrams for: ")
        start = time.time()
        word_lst = read_dictionary()
        if s != EXIT:
            # Find and display anagrams if the input is not the EXIT command
            find_anagrams(s, word_lst)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')
        else:
            # Exit the loop if the EXIT command is entered
            break
        ####################



def read_dictionary():
    """
    Reads the dictionary file and converts it into a list of words.
    This makes it easier to search for anagrams within the dictionary.
    :return word_lst: list, a list of words from the dictionary file.
    """
    word_lst = []
    with open(FILE, "r") as f:
        # Process each line in the dictionary file
        for line in f:
            # Extract word, remove newline character, and add to word list
            word = line.split("\n")[0]
            word_lst.append(word)
        return word_lst


def find_anagrams(s, word_lst):
    """
    Finds all anagrams of the user's input word using a helper function.
    It also initializes a list to keep track of characters used in forming anagrams.

    Args:
        s (str): The input word from the user.
        word_lst (list): The list of words from the dictionary.

    Returns:
        list: A list of all anagrams for the input word.
    """
    #Initialize a list to track which characters have been used
    used = []
    for i in range(len(s)):
        used.append(False)

    # Call helper function to find anagrams and print the results
    anagrams = find_anagrams_helper(s, word_lst, "", used, [])
    print(f'{len(anagrams)} anagrams: {anagrams}')


def find_anagrams_helper(s, word_lst, partial, used, current_anagrams):
    """
    Recursive helper function to find anagrams. It builds potential anagrams character
    by character and checks if they are valid anagrams.

    Args:
        s (str): The input word from the user.
        word_lst (list): The list of words from the dictionary.
        partial (str): Current partial anagram being built.
        used (list of bool): Tracks which characters from the input word have been used.
        current_anagrams (list): Accumulates the valid anagrams found so far.

    Returns:
        list: Updated list of all valid anagrams found.
    """
    anagrams = [] # Create an empty list to save the result of final anagrams

    # Base case: if partial word length matches input word length
    if len(partial) == len(s):
        # Check if the partial word is a valid anagram and not already found
        if partial in word_lst and partial not in current_anagrams:
            current_anagrams.append(partial)
            print(f'Found: {partial}')
            print(f'Searching...')

    else:
        # Iterate through each character of the input word
        for i in range(len(s)):
            if not used[i]: # Check if the character is not already used

                # Choose: mark the character as used and add to the partial word
                used[i] = True
                partial += s[i]

                # Explore: continue searching if the partial word has a valid prefix
                if has_prefix(partial, word_lst):
                    find_anagrams_helper(s, word_lst, partial, used, current_anagrams)

                # Un-choose: revert the last choice before next iteration
                used[i] = False
                partial = partial[:-1]

    return current_anagrams  # Return the list of found anagrams


def has_prefix(sub_s, word_lst):
    """
    Checks if any word in the dictionary starts with the given prefix.
    This is used to early-stop the search if the current partial word cannot
    lead to a valid anagram.

    Args:
        sub_s (str): The prefix to check in the dictionary.
        word_lst (list): The list of words from the dictionary.

    Returns:
        bool: True if the prefix is found in the dictionary, False otherwise.
    """
    prefix = False

    # Check each word in the dictionary for the given prefix
    for word in word_lst:
        # If a word with the prefix is found, return True
        if word.startswith(sub_s):
            prefix = True
            break
    return prefix

if __name__ == '__main__':
    main()

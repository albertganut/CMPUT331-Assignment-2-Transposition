#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 Albert Ganut
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 2 Student Solution
September 2026
Author: Albert Ganut
"""

import math

def encipherMessage(key: int, message: str) -> str:

    ciphertext = [""] * key # initializes an empty list of strings the size of the key 

    for column in range(key):

        current_index = column

        while current_index < len(message): # runs as long as we still have characters to go through
            ciphertext[column] += message[current_index] # add the character at the current index to the current column
            current_index += key # go to the next character in the current column

    return "".join(ciphertext) 

def decipherMessage(key: int, message: str) -> str:

    num_of_cols = int(math.ceil(len(message) / float(key))) # calculates how many columns we need to create the grid by dividing the length of the message by the key and rounding up to the nearest int
    num_of_rows = key # sets the HEIGHT of the grid
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(message)

    plaintext = [""] * num_of_cols # initializes an empty list of strings the size of the number of columns

    col = 0
    row = 0

    for symbol in message: # loops through the ciphertext 
        plaintext[col] += symbol # adds the current symbol to the current column in the plaintext list
        col += 1

        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes): # runs if we've reached the end of a column, or if we're at the last column and we've reached the last row that's not shaded
            col = 0 # go back to the first column
            row += 1 # go to the next row

    return "".join(plaintext)

def test():
    assert encipherMessage(5, "CIPHERS ARE FUN") == "CREIS P FHAUERN"
    assert decipherMessage(2, encipherMessage(2, "SECRET")) == "SECRET"
    assert decipherMessage(3, encipherMessage(3, "CIPHERS ARE FUN")) == "CIPHERS ARE FUN"
    assert decipherMessage(4, encipherMessage(4, "HELLO WORLD")) == "HELLO WORLD"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()

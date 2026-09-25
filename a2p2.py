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

from typing import List

def encipherMessage(key: List[int], message: str) -> str:

    ciphertext = [] # will hold the final ciphertext as a list of strings

    for col_num in key: # go through each col that's associated with the key

        current_index = col_num - 1 
        col_str = "" # holds the string for the current column

        while current_index < len(message): # runs if the current index is still within the bounds (the length) of the message
            col_str += message[current_index] # add the character at the current index to the col_str
            current_index += len(key)

        ciphertext.append(col_str)

    return "".join(ciphertext)

def test():
    assert encipherMessage([2, 4, 1, 5, 3], "CIPHERS ARE FUN") == "IS HAUCREERNP F"


from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()

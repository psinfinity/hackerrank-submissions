# https://www.hackerrank.com/challenges/capitalize/problem
import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    output = ""
    new_word = False
    for letter in s:

        if new_word or letter == s[0]:
            output += letter.title()
            new_word = False
        else:
            output += letter

        if letter == ' ':
            new_word = True

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

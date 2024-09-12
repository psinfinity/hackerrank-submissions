# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

t_count = int(input())
for i in range(t_count):
    new_input = input()
    try:
        re.compile(new_input)
        print("True")
    except re.error:
        print("False")

# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

given_input = input().split()
given_input[0] = sorted(''.join(sorted([i for i in given_input[0]])))
for i in combinations_with_replacement(given_input[0], int(given_input[1])):
    print(''.join(i))
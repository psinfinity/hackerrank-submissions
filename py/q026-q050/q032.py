# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
given_input = input().split()

for i in sorted(list(permutations(given_input[0], int(given_input[1])))):
    print(''.join(i))
# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

given_input = input().split()
given_input[0] = sorted(''.join(sorted([i for i in given_input[0]])))
for j in range(1,1+int(given_input[1])):
    for i in list(combinations(given_input[0], j)):
        print(''.join(i))
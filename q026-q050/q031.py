# https://www.hackerrank.com/challenges/itertools-product/problem

matrix_a = [int(x) for x in input().split()]
matrix_b = [int(x) for x in input().split()]
for i in matrix_a:
    for j in matrix_b:
        print((i, j), end=" ")
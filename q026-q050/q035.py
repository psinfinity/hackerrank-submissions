# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby
giveninput=input()
for k, g in groupby(giveninput):
    print((len(list(g)), int(k)), end=' ')
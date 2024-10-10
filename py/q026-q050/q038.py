# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

n = int(input())

Student = namedtuple('Student', ", ".join(input().split()))
mark_sum = 0
for i in range(n):
    x = input().split()
    child = Student(x[0], x[1], x[2], x[3])
    mark_sum += int(child.MARKS)

print(mark_sum / n)
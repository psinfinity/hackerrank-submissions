# https://www.hackerrank.com/challenges/symmetric-difference/problem

m_count = int(input())
m = [int(x) for x in input().split()]
n_count = int(input())
n = [int(x) for x in input().split()]

xor_list = sorted(list(set(n+m)))

for i in xor_list:
    if not(i in n and i in m):
        print(i)
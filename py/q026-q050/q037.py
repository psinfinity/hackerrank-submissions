# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

nm = [int(x) for x in input().split()]
n_list = []
m_list = []
for _ in range(nm[0]):
    n_list.append(input())
for _ in range(nm[1]):
    m_list.append(input())

for i in m_list:
    for j in range(len(n_list)):
        if i == n_list[j]:
            print(j+1, end=" ")
    if i not in n_list:
        print(-1, end="")
    print()


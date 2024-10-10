# https://www.hackerrank.com/challenges/designer-door-mat/problem

giveninput = [int(i) for i in input().split()]

n = giveninput[0]
m = giveninput[1]


for row in range(1,int((n-1)/2)+1):
    print(('.|.'*(2*row - 1)).center(m,'-'))

print('WELCOME'.center(m,'-'))

for row in range(int((n-1)/2)):
    print(('.|.'*(2*(int((n-1)/2) - row) - 1)).center(m,'-'))
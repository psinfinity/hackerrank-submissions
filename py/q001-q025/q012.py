# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    mylist = []
    for _ in range(N):
        user_input = input().split()
        if user_input[0] == 'insert':
            mylist.insert(int(user_input[1]), int(user_input[2]))
        if user_input[0] == 'print':
            print(mylist)
        if user_input[0] == 'remove':
            mylist.remove(int(user_input[1]))
        if user_input[0] == 'append':
            mylist.append(int(user_input[1]))
        if user_input[0] == 'sort':
            mylist.sort()
        if user_input[0] == 'pop':
            mylist.pop()
        if user_input[0] == 'reverse':
            mylist = mylist[::-1]

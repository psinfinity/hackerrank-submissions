# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    mylist = set(arr)
    mylist = list(mylist)
    mylist.sort(reverse=True)

    print(mylist[1])


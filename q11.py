# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    i = 0.00
    for r in range(3):
        i = i + student_marks[query_name][r]
    print(format(i / 3, ".2f"))

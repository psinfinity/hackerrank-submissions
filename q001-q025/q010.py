# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []
    recordset = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append((name, score))
        recordset.append(score)

    recordset = set(recordset)

    recordset = list(recordset)
    recordset.sort()
    least2 = recordset[1]

    records.sort(key=lambda x: x[0])
    for (a, b) in records:
        if b == least2:
            print(a)






# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    n = len(string)
    partition_size = int(n / k)
    j = 0
    while j < partition_size:
        output = ''
        i = 0
        while i < k:
            if not string[j * k + i] in output:
                output += string[j * k + i]
            i += 1

        print(output)
        j += 1


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
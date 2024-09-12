# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    int_input = int(input())
    arr_input = input().split()
    temp_list = []
    for i in range(int_input):
        temp_list.append(int(arr_input[i]))

    print(hash(tuple(temp_list)))

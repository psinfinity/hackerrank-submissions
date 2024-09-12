# https://www.hackerrank.com/challenges/exceptions/problem

if __name__ == '__main__':
    test_case_count = int(input())
    for i in range(test_case_count):
        arr=input().split()
        try:
            print(int(int(arr[0])/int(arr[1])))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:",e)

# https://www.hackerrank.com/challenges/any-or-all/problem

user_input = [int(input()), input().split()]
if any([True for i in user_input[1] if str(i)[:int((len(str(i))+1)/2):] == str(i)[:int(len(str(i))/2)-1:-1]]) or any([len(str(i))==1 for i in user_input[1]]) and all(int(i)>0 for i in user_input[1]): print(True)
else: print(False)
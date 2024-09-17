# https://www.hackerrank.com/challenges/word-order/problem

word_list = dict()
for _ in range(int(input())):
    x = input()
    if x in word_list.keys():
        word_list[x]+=1
    else:
        word_list[x] = 1
print(len(word_list.values()))
for i in list(word_list.values()):
    print(i,end=" ")
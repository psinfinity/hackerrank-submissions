# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# as of python 3.7 this cmd is not necessary as dictionaries are now ORDERED

mydict = dict()
for _ in range(int(input())):
    k=input()
    if k in mydict.keys():
        mydict[k] +=1
    else:
        mydict[k] = 1

for i in mydict.keys():
    print(" ".join(i.split()[:-1]), int(i.split()[-1])*int(mydict[i]))
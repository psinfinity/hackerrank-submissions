# https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    stuart_count = 0
    kevin_count = 0
    vowels = 'AEIOU'

    for i in range(len(string)):
        if string[i] in vowels:
            kevin_count += (len(string) - i)
        else:
            stuart_count += (len(string) - i)

    if stuart_count > kevin_count:
        print(f'Stuart {stuart_count}')
    elif stuart_count < kevin_count:
        print(f'Kevin {kevin_count}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)


# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    i=0
    k=1
    while 0 <= i < size:
        l = 1
        j = 0
        temp_string = ""
        while 0 <= j <= i:
            temp_string += chr(97 + size - j - 1)
            if j == i:
                l = -1
            if i != size - 1 or j != 0 or l == 1:
                temp_string += "-"
            j+=l

        i += k
        if i == size - 1:
            k = -1
        print(temp_string.center(4*size-3,'-'))




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
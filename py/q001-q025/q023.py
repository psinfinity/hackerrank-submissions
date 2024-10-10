import textwrap

def wrap(string, max_width):
    result = ""

    for i in range(len(string)):
        result+=string[i]
        if (i+1)%max_width == 0:
            result+='\n'
    
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



# -- author: lijw --
if __name__ == '__main__':
    while True:
        a, b, c = input().split(' ')
        a = int(a)
        b = int(b)
        c = int(c)
        if a == 0 and b == 0 and c == 0:
            break
        print(pow(a, b, c))

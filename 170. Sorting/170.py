
# -- author: lijw --
if __name__ == '__main__':
    n = input().split(' ')
    s = set()
    for x in n:
        now = int(x)
        if now != 0:
            s.add(now)
    s = list(s)
    s.sort()
    for x in s:
        print(x, end=' ')

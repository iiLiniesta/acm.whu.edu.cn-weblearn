def is_start(s):
    a = s.split(':')
    try:
        assert 2 == len(a)
        x = int(a[0])
        y = int(a[0])
    except:
        return False
    return True


now = 0
prefix = ''


def accum(l, now):
    for x in l:
        if 0 < len(x) and x[0].isalpha():
            now += 1
    return now

try:
    while True:
        s = input().split(' ')
        if is_start(s[0]):
            if '' != prefix:
                print(prefix, now)
            prefix = s[0]
            now = 0
            now = accum(s[1:], now)
        else:
            now = accum(s, now)
except EOFError:
    print(prefix, now)
    pass

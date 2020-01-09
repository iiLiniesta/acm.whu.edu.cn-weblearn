d = {
    1: 1,
    2: 2,
    3: 8,
    4: 3,
    5: 6,
}

def calc(n):
    global d
    if n not in d:
        if n & 1:
            ans = calc(3 * n + 1) + 1
        else:
            ans = calc(n // 2) + 1
        d[n] = ans
    return d[n]


def work(a, b):
    if a > b:
        c = a
        a = b
        b = c
    ans = 0
    for n in range(b, a-1, -1):
        ans = max(ans, calc(n))
    return ans


# -- author: lijw --
if __name__ == '__main__':
    while True:
        a, b = input().split(' ')
        a = int(a)
        b = int(b)
        if 0 == a and 0 == b:
            break
        print(work(a, b))

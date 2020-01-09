
def to3(n):
    ans = []
    while n:
        ans.append(n % 3)
        n //= 3

    def xxx(i, t):
        while True:
            try:
                ans[i] += t
                break
            except IndexError:
                ans.append(0)
    i = 0
    while i < len(ans):
        if ans[i] >= 3:
            xxx(i+1, ans[i]//3)
            ans[i] %= 3
        if ans[i] == 2:
            ans[i] = -1
            xxx(i+1, 1)
        i += 1

    # print(ans)
    ans.reverse()
    s = ''
    for x in ans:
        s += str(x)[0]
    return s


def test():
    n = int(input())
    if 0 == n:
        return 0
    s = to3(abs(n))
    if n < 0:
        s = s.replace('1', '*')
        s = s.replace('-', '1')
        s = s.replace('*', '-')
    return s


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

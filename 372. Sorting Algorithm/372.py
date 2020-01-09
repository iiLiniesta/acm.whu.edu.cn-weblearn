
def work(n, m):
    s = []
    for i in range(n):
        s.append(int(input()))
    s.sort()
    ans = str(s[0])
    for i in range(m, n, m):
        ans += ' %d' % s[i]
    print(ans)


# -- author: lijw --
if __name__ == '__main__':
    while True:
        n, m = input().split(' ')
        n = int(n)
        m = int(m)
        if 0 == n and 0 == m:
            break
        work(n, m)

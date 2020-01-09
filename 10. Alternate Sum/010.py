MOD = 2006
def work(n):
    if 1 == n:
        s = [int(input())]
    else:
        s = input().split(' ')
        for i in range(n):
            s[i] = int(s[i])
    s.sort()
    return (s[-1] * pow(2, n - 1, MOD)) % MOD


# -- author: lijw --
if __name__ == '__main__':
    while True:
        n = int(input())
        if 0 == n:
            break
        print(work(n))

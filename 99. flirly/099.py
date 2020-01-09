
# -- author: lijw --
if __name__ == '__main__':
    while True:
        try:
            n, m = input().split(' ')
            n = int(n)
            m = int(m)
        except EOFError:
            break
        ans = pow(2, n, m) - 1
        ans %= m
        print(ans)


def work(n):
    for _ in range(n):
        s = input().split(' ')
        for x in s:
            x = int(x)
            ans = 0
            while x > 0:
                ans ^= x & 1
                x >>= 1
            print(ans, end=' ')
        print()


    return 0


# -- author: lijw --
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        work(n)

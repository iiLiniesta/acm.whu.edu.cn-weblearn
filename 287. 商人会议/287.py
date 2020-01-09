

ans = {
    0: 1,
    2: 1,
    4: 2,
}
for n in range(6, 60, 2):
    now = 0
    for i in range(0, n, 2):
        now += ans[i] * ans[n-2-i]
    ans[n] = now

def work(n):
    if n & 1:
        return 0
    return ans[n]


# -- author: lijw --
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        print(work(n))

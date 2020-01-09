a = {
2: [2],
3: [3],
4: [2, 2],
}
def work(n):
    if n <= 3:
        print(n)
        return

    n1 = n // 3
    n2 = n % 3
    if n2 != 2:
        n2 += 3
        n1 -= 1

    ans = a[n2] + [3] * n1
    for i in range(len(ans)-1):
        print(ans[i], end=' ')
    print(ans[-1])


# -- author: lijw --
if __name__ == '__main__':
    while True:
        n = int(input())
        if 0 == n:
            break
        work(n)

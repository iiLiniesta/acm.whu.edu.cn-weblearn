
N = 6
a = []
flag = [0] * N
flag2 = [0] * (N * (N-1) // 2 + 1)


def calc():
    global a
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if a[i] > a[j]:
                ans += 1
    return ans

def test(i):
    global a, flag
    if i == N:
        ans = calc()
        if flag2[ans] == 0:
            print(a, ans)
            flag2[ans] = 1
        return
    for j in range(N):
        if flag[j] == 0:
            a.append(j)
            flag[j] = 1
            test(i+1)
            a.pop()
            flag[j] = 0
    return 0


# -- author: lijw --
if __name__ == '__main__':
    test(0)
    # T = int(input())
    # for _ in range(T):
    #     print(test())

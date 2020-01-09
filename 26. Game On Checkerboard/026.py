
def test():
    n = int(input())

    line = input().split(' ')
    ans = []
    for i in range(n):
        ans.append(int(line[i]))

    for _ in range(1, n):
        line = input().split(' ')
        now = []
        for i in range(n):
            now.append(int(line[i]))
        for i in range(n):
            max_pre = ans[i]
            if i > 0:
                max_pre = max(max_pre, ans[i-1])
            if i < n - 1:
                max_pre = max(max_pre, ans[i+1])
            now[i] += max_pre
        ans = now
    return max(ans)


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        if i > 0:
            print()
        print('Case %d:' % (i + 1))
        print(test())

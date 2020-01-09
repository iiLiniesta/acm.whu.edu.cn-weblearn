
def test():
    n = int(input())
    a = input().split(' ')
    for i in range(n):
        a[i] = int(a[i])
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                ans += 1
    return ans


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

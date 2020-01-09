
def test():
    n = int(input())
    b = input().split(' ')
    a = []
    for i in range(n):
        a.append(int(b[i]))
    a.sort()
    for i in range(n-1, -1, -1):
        l = 0
        r = i - 1
        while r > l:
            if a[l] + a[r] < a[i]:
                l += 1
            elif a[l] + a[r] > a[i]:
                r -= 1
            else:
                return a[i]
    return -1


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

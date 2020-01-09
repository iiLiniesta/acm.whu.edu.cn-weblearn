
def test():
    n = int(input())
    ans = 0
    a = []
    for i in range(n):
        x, y = input().split(' ')
        a.append((int(x), int(y)))
    for i in range(n-1):
        x1, y1 = a[i]
        x2, y2 = a[i+1]
        ans += x1 * y2 - x2 * y1
    x1, y1 = a[n-1]
    x2, y2 = a[0]
    ans += x1 * y2 - x2 * y1
    return int(ans/2)


# -- author: lijw --
if __name__ == '__main__':
    print(test())

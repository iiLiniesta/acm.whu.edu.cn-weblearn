
def test():
    a, b, k = input().split(' ')
    k = int(k)
    n = len(a)
    s = []
    for i in range(n):
        s.append(abs(ord(a[i])-ord(b[i])))
    s.sort()
    s.reverse()
    i = 0
    while i < k and s[i] > 0:
        i += 1
    ans = sum(s[i:])
    ans += k - i
    return ans


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

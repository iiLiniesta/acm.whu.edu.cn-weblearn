
def test():
    m = int(input())
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = input().split(' ')
        a = int(a)
        b = int(b)
        # ans = (ans + pow(a, b, m)) % m
        ans += pow(a, b, m)
    return ans % m


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

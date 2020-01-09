from Crypto.Util.number import bytes_to_long as b2l
from Crypto.Util.number import long_to_bytes as l2b

def bs(n):
    # Calc how many zero bytes at the end of n
    pass


def work(n):
    a = [0xff] * (n + 1)
    for _ in range(n):
        num, name = input().split(' ')
        num = int(num)
        name = b2l(l2b(_) + bytes(name[::-1], encoding='ascii'))
        a[num] = name
    m = int(input())
    for _ in range(m):
        q = int(input())
        ans = 0
        for j in range(q):
            x, y = input().split(' ')
            x = int(x)
            y = int(y)
            cmp = a[x] ^ a[y]
            # print(hex(cmp))
            while 0 == (cmp & 0xff):
                cmp >>= 8
                ans += 1
        print(ans)


def work2(n):
    a = [0] * (n + 1)
    for _ in range(n):
        num, name = input().split(' ')
        num = int(num)
        a[num] = name
    m = int(input())
    for _ in range(m):
        q = int(input())
        ans = 0
        for j in range(q):
            x, y = input().split(' ')
            x = int(x)
            y = int(y)
            for k in range(min(len(a[x]), len(a[y]))):
                if a[x][k] != a[y][k]:
                    break
            ans += k
        print(ans)


# -- author: lijw --
if __name__ == '__main__':
    n = int(input())
    work2(n)

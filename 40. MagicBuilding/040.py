def test():
    T = int(input())
    for _ in range(T):
        n = int(input())
        str = input()
        a = str.split(' ')
        s = set()
        d = dict()
        ans = 0
        for x in a:
            if x not in s:
                s.add(x)
                d[x] = 0
            d[x] += 1
            if d[x] > ans:
                ans = d[x]
        print(ans)


# -- author: lijw --
if __name__ == '__main__':
    test()

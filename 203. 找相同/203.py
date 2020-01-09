
def work1(n, s):
    s = list(map(int, s))
    counter = 1
    ans = s[0]
    for i in range(1, len(s)):
        now = s[i]
        if now == ans:
            counter += 1
        else:
            counter -= 1
        if counter <= 0:
            counter = 1
            ans = now
    return ans


def work2(n, s):
    s = list(map(int, s))
    d = dict()
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
        if d[x] * 2 > n:
            return x


# -- author: lijw --
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            s = input().split(' ')
        except EOFError:
            break
        print(work2(n, s))


def work(s):
    ans = ''
    for i in range(len(s)):
        if i & 1:
            ans += s[i].upper()
        else:
            ans += s[i]
    return ans


# -- author: lijw --
if __name__ == '__main__':
    i = 0
    while True:
        s = input()
        if s == '#':
            break
        i += 1
        print("Case %d:" % i, work(s))

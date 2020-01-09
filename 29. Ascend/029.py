
def work(s):
    now = 1
    ans = ''
    for i in range(len(s)):
        c = ord(s[i]) - 65
        m = (c - now) % 26
        ans += chr(m + 65)
        now += 1
    print(ans)


# -- author: lijw --
if __name__ == '__main__':
    while True:
        s = input()
        if '$' == s:
            break
        work(s)

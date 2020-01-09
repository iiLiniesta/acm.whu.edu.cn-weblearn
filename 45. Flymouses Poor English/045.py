
def test():
    s = input()
    ans = s[0].upper()
    for i in range(1, len(s)):
        now = s[i]
        if now.isupper() and ' ' != s[i-1]:
            now = now.lower()
        ans += now
    return ans


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

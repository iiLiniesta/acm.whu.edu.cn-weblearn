
def test():
    s1 = input()
    s2 = input()
    len1 = len(s1)
    len2 = len(s2)
    table = [0 for i in range(len2+1)]
    ans = 0
    for i in range(len1):
        for j in range(len2-1, -1, -1):
            if s1[i] == s2[j]:
                if i == 0 and j == 0:
                    table[j] = 1
                else:
                    table[j] = table[j-1] + 1
            else:
                table[j] = 0
            ans = max(ans, table[j])
    return ans


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

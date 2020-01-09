
def upper_in(s):
    for i in range(ord('A'), ord('Z')+1):
        if chr(i) in s:
            return True
    return False


def work(s):
    if s[0].isupper() or ('_' in s and upper_in(s)) or s[-1]=='_' or s[0]=='_':
        return 'Error!'
    ans = ''
    if upper_in(s):  # java
        for x in s:
            if x.isupper():
                ans += '_' + x.lower()
            else:
                ans += x
    elif '_' in s:  # C++
        flag = False
        for x in s:
            if x == '_':
                if flag:
                    return 'Error!'
                flag = True
            elif flag:
                ans += x.upper()
                flag = False
            else:
                ans += x
    else:
        ans = s
    return ans


# -- author: lijw --
if __name__ == '__main__':
    print(work(input()))

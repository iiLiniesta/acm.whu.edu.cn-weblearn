
def test():
    s = input()
    height = 0
    length = 0
    ans = 0.0
    for x in s:
        if x == 'R':
            length += 1
            ans -= height
        elif x == 'U':
            height += 1
    ans += height * length / 2

    return "%.3f" % ans


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())


def test():
    n = int(input())
    ans = 1
    for _ in range(n):
        ans = ans * 4 - 1
    return ans


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

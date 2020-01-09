
def work(n):
    ans = 0
    for _ in range(n * 2 + 1):
        ans ^= int(input())
    return ans


# -- author: lijw --
if __name__ == '__main__':
    n = int(input())
    print(work(n))

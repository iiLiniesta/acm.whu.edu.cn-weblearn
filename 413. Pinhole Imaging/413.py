
def test():
    a,b,h = map(int, input().split(' '))
    return "%.2f" % (h * b / a)


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())


def test():
    p = float(input()[:-1])/100
    x = 2 * p * (1 - p)
    ans = p * p / (1 - x)
    return ('%.2f' % (ans * 100)) + '%'


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

import datetime
time0 = datetime.date(2018, 8, 8)

def test():
    # md = input()
    m, d = input().split(' ')
    m = int(m)
    d = int(d)
    time1 = datetime.date(2018, m, d)
    return time0.__sub__(time1).days


    return 0


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

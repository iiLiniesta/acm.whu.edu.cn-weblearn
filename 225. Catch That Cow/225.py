
def work(n, k):
    map = [0] * 200000
    step = 0
    s = set()
    s.add(n)
    map[n] = 1
    while map[k] == 0:
        step += 1
        now = set()
        for x in s:
            if x+1 <= 100000 and map[x + 1] == 0:
                now.add(x + 1)
                map[x + 1] = 1
            if x-1 >= 0 and map[x - 1] == 0:
                now.add(x - 1)
                map[x - 1] = 1
            if x*2 <= 100000 and map[x * 2] == 0:
                now.add(x * 2)
                map[x * 2] = 1
        s = now
    return step


# -- author: lijw --
if __name__ == '__main__':
    n, k = input().split(' ')
    n = int(n)
    k = int(k)
    print(work(n, k))

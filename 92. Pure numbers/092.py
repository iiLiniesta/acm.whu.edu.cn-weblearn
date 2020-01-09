
n=5000000

def test():
    l = [0]*n
    l[0] = 1
    l[1] = 1
    result = []
    for i in range(2, n):
        if l[i] == 0:
            result.append(i)
            for j in range(i + i, n, i):
                l[j] = 1
            now = i * i
            while now < n:
                result.append(now)
                now *= i
    result.sort()
    #print(len(result))
    #print(result[:40])
    while True:
        try:
            x = input()
        except EOFError:
            break
        x = int(x)
        if x>348940:
            print(-1)
        else:
            print(result[x-1])


# -- author: lijw --
if __name__ == '__main__':
    test()

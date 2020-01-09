
def work(n):
    s = input().split(' ')
    ans = 0
    count = 0
    for x in s:
        if x == '1':
            count += 1
        elif x == '-1':
            ans += count
    print(ans)


# -- author: lijw --
if __name__ == '__main__':
    T = 0
    while True:
        n = int(input())
        if n == -1:
            break
        T += 1
        print("Case " + str(T) + ": ", end='')
        work(n)

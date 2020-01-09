
def work(m, n):
    ans = []
    for _ in range(n):
        ans.append([])
    row_now = m
    col_now = m
    gap_start = 2
    for i in range(n):
        ans[i].append(col_now)
        gap = gap_start
        row_now = col_now
        for j in range(n-gap_start+1):
            row_now += gap
            ans[i].append(row_now)
            gap += 1
        col_now += gap_start - 1
        gap_start += 1

    for i in range(n-1, -1, -1):
        for x in ans[i]:
            print("%2d " % x, end = '')
        print()
    print()


# -- author: lijw --
if __name__ == '__main__':
    while True:
        m, n = input().split()
        m = int(m)
        n = int(n)
        if m <= 0 and n <= 0:
            break
        work(m, n)

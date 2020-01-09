
INF = 0xffffffff

def test():
    n = int(input())
    mat = []
    d = dict()
    for i in range(n):
        temp = input().split(' ')
        line = []
        for j in range(n):
            now = int(temp[j])
            if i > j:
                now = min(now, mat[j][i])
            line.append(now)
        mat.append(line)
        d[i] = INF
    ans = 0
    while len(d) > 0:
        for x in d:
            nearest = x
            break
        for x in d:
            # print(x, d[x], nearest,d[nearest])
            if d[x] < d[nearest]:
                nearest = x
        new_dist = d.pop(nearest)
        if new_dist < INF:
            ans += new_dist
        # print(nearest, new_dist)
        for x in d:
            d[x] = min(mat[nearest][x], d[x])
        # print(d)

    return ans


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

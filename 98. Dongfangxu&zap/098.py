
ans = ['zap', 'dongfangxu']
d = {'0': 0, '1': 1}

def test():
    s = input().replace(ans[0], '0').replace(ans[1], '1')
    fin = [0] * 2
    stat = [0] * 2
    for i in s:
        if i not in d:
            stat = [0] * 2
            continue
        now = d[i]
        stat[0] = (1-now) * stat[0] + (1-now)
        stat[1] = now * stat[1] + now
        fin[0] = max(fin[0], stat[0])
        fin[1] = max(fin[1], stat[1])

    return (ans[fin[1]>=fin[0]]+'!')


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

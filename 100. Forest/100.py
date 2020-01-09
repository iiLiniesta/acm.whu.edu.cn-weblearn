# ?littleken","knuthocean","dongfangxu","zap","kittig","robertcui","forest","flirly"。
ans = ['littleken', 'knuthocean', 'dongfangxu', 'zap', 'kittig', 'robertcui', 'forest', 'flirly']
d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7}
dd = ['0', '1', '2', '3', '4', '5', '6', '7']

def test():
    s = input()
    for i in range(8):
        s = s.replace(ans[i], dd[i])
    now_max = 0
    now_person = ''
    stat = [0] * 8
    for i in s:
        if i not in d:
            continue
        now = d[i]
        stat[now] += 1
        if stat[now] > now_max:
            now_max = stat[now]
            now_person = ans[now]

    return now_person


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

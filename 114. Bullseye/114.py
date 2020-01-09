def score(x,y):
    r = 3
    d2 = x * x + y * y
    while r * r < d2 and r <= 15:
        r += 3
    ans = (6 - (r // 3)) * 20
    return ans


def work(s):
    a1 = 0
    for i in range(0,6,2):
        a1 += score(s[i], s[i+1])
    a2 = 0
    for i in range(6,12,2):
        a2 += score(s[i], s[i+1])
    ans = "SCORE: %d to %d, " % (a1, a2)
    if a1 > a2:
        ans += "PLAYER 1 WINS."
    elif a1 < a2:
        ans += "PLAYER 2 WINS."
    else:
        ans += "TIE."

    return ans


# -- author: lijw --
if __name__ == '__main__':
    while True:
        s = list(map(float, input().split(' ')))
        if s[0] == float(-100):
            break
        print(work(s))

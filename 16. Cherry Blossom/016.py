
ans = ['NO', 'YES']

def work(n):
    all_set = set()
    top_set = set()
    bot_set = set()
    for i in range(n):
        x, y = input().split(' ')
        x = int(x)
        y = int(y)
        all_set.add((x, y))
        if len(top_set) > 0:
            sample_top = list(top_set)[0][1]
            if y > sample_top:
                top_set = set()
                top_set.add((x, y))
            elif y == sample_top:
                top_set.add((x, y))
        else:
            top_set.add((x, y))

        if len(bot_set) > 0:
            sample_bot = list(bot_set)[0][1]
            if y < sample_bot:
                bot_set = set()
                bot_set.add((x, y))
            elif y == sample_bot:
                bot_set.add((x, y))
        else:
            bot_set.add((x, y))

    if len(top_set) != len(bot_set):
        return 0
    sample_top = list(top_set)[0][1]
    sample_bot = list(bot_set)[0][1]
    doublemid = sample_bot + sample_top
    for x, y in all_set:
        try:
            assert 2 * y == doublemid or (x, doublemid-y) in all_set
        except AssertionError:
            return 0

    return 1


# -- author: lijw --
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(ans[work(n)])
        except EOFError:
            break

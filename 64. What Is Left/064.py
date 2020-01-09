
def work(n):
    a = input().split(' ')
    s = set()
    for x in a:
        s.add(int(x))
    s = list(s)
    s.sort()
    for i in range(len(s)-1):
        print(s[i],end=' ')
    print(s[-1])



# -- author: lijw --
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        work(n)

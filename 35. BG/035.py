
def work(n):
    print((n+1)>>1)


# -- author: lijw --
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if 0 == n:
                break
            work(n)
        except:
            break

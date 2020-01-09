
def work(n):
    print((n*n*n+5*n+6)//6)


# -- author: lijw --
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            work(n)
        except EOFError:
            break

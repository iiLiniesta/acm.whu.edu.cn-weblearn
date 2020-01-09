
def test():
    n = int(input())
    if n % 7 < 2:
        return "Dzs"
    else:
        return "Sproblvem"


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

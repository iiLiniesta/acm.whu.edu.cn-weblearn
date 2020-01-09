
def test():
    n = int(input())
    if 0 == n % 14:
        return 'snoopy wins the game!'
    else:
        return 'flymouse wins the game!'


# -- author: lijw --
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(test())

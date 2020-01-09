
d = {
    '0': 1,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 1,
    '5': 0,
    '6': 1,
    '7': 0,
    '8': 2,
    '9': 1,
    'A': 1,
    'B': 2,
    'C': 0,
    'D': 1,
    'E': 0,
    'F': 0,
}
def fun(k):
    return d[k]

# -- author: lijw --
if __name__ == '__main__':
    n = int(input())
    s = hex(n)[2:].upper()
    print(sum(map(fun, s)))

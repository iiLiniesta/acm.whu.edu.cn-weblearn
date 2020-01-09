book = {
    'A': 'V',
    'B': 'W',
    'C': 'X',
    'D': 'Y',
    'E': 'Z',
    'F': 'A',
    'G': 'B',
    'H': 'C',
    'I': 'D',
    'J': 'E',
    'K': 'F',
    'L': 'G',
    'M': 'H',
    'N': 'I',
    'O': 'J',
    'P': 'K',
    'Q': 'L',
    'R': 'M',
    'S': 'N',
    'T': 'O',
    'U': 'P',
    'V': 'Q',
    'W': 'R',
    'X': 'S',
    'Y': 'T',
    'Z': 'U',
}


def test():
    while True:
        start = input()
        if start == 'ENDOFINPUT':
            break
    
        cipher = input()
        for c in cipher:
            if c in book:
                c = book[c]
            print(c, end='')
        print()
        
        end = input()


# -- author: lijw --
if __name__ == '__main__':
    test()

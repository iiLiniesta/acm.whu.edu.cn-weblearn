import numpy
from fractions import Fraction
import time
import math

tri = []
Sn = []
M = 20


def pre_work():
    global tri
    global Sn
    now_line = [Fraction(1, 1)] + [(Fraction(0, 1))] * (M+1)
    tri.append(now_line)
    for i in range(1, M+2):
        now_line = [Fraction(1, 1)]
        for j in range(1, M+2):
            # print(i, j, now_line)
            now_line.append(Fraction(tri[i-1][j-1] + tri[i-1][j], 1))
        tri.append(now_line)
    tri_mat = numpy.mat(tri)

    now_line = [Fraction(0, 1), Fraction(1, 1)] + [(Fraction(0, 1))] * (M)
    one = numpy.mat([Fraction(1, 1)] + [(Fraction(0, 1))] * (M+1))

    Sn.append(now_line)
    Sn_mat = [numpy.mat(Sn[0])]
    for i in range(1, M+1):
        now_line = tri_mat[i+1] - one
        for j in range(i):
            now_line -= tri[i+1][j] * Sn_mat[j]
        now_line = now_line/tri[i+1][i]
        Sn_mat.append(now_line)
        Sn.append(Sn_mat[i].tolist()[0])

    # Sn_mat = numpy.mat(Sn)
    for i in range(len(Sn)):
        # print(Sn[i])
        pass


def work(n, m):
    ans = 0
    now = 1
    for i in range(len(Sn[m])):
        ans += now * Sn[m][i]
        # print(ans)
        now *= n
    return int(ans)


def check():
    f = open("result_py.txt", "w")
    start = time.time()
    for n in range(1, 100000+1):
        for m in range(1, 21):

            ans = work(n, m)
            ans = format(ans,'.2E').replace('+', '').replace('E0', 'E')
            print("{%8d,\t%2d,\t%s},"%(n,m,ans), file=f)
        if 0 == n % 10000:
            end = time.time()
            duration = end - start
            print("n =", n, ",\tTIME:", duration, "s")
        # print(format(ans,'.2E').replace('+', ''))
    f.close()


# -- author: lijw --
if __name__ == '__main__':
    pre_work()
    while True:
        try:
            x = input().split(' ')
        except:
            break
        n = int(x[0])
        m = int(x[1])
        ans = work(n, m)
        #print(ans)
        power = int(math.log(ans, 10))
        ans = (int((ans//(10**(power-3)))/10 + 0.5))/100
        print("%.2fE%d"%(ans,power))
        # print(format(ans,'.2E').replace('+', ''))

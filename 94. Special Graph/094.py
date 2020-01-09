
init = [[3, -1], [1, 0]]
I = [[1, 0], [0, 1]]

def mat_mul(m1, m2):
    ans = [
        [m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0], m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1]],
        [m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0], m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1]],
    ]
    return ans


def mat_pow(now, p):
    if 0 == p:
        return I
    sq = mat_pow(now, p>>1)
    if 1 == p & 1:
        return mat_mul(mat_mul(sq, sq), now)
    else:
        return mat_mul(sq, sq)


def work(n):
    # Alg 1.
    # f[0]=1, f[1]=1
    # n>=2: f[n] = f[n-1] + sum[1..(n-1)]

    # Alg 2.
    # f[0]=0, f[1]=1
    # n>=2: f[n] = 3 * f[n-1] - f[n-2]
    f = [0, 1]
    if n < 2:
        return f[n]
    mat = mat_pow(init, n-1)
    # print(mat[0][0])
    v = mat[0][0]
    ans = 0
    while v > 0:
        v //= 10
        ans += 1
    return ans


# -- author: lijw --
if __name__ == '__main__':
    '''
    for i in range(10, 1001, 10):
        print("i={}\t, ans={}".format(i, work(i)))
    '''
    while True:
        try:
            n = int(input())
        except:
            break
        print(work(n))

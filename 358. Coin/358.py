def gcd(a, b):
    if 0 == b:
        return a
    return gcd(b, a % b)


def test(p, q):
    if p > q:
        t = p
        p = q
        q = t
    x = pow(p, q-2, q)  # x=p^(-1) mod q
    y = pow(q, p-2, p)  # y=q^(-1) mod p
    a = (x * p) // q  # x*p-a*q=1
    b = (y * q) // p  # y*q-b*p=1

    g = gcd(a, y)
    lcm = (a * y) // g

    left = lcm // a
    right = lcm // y
    tot = left + right

    s = 0
    t = 0
    ansleft = 0
    ansright = 0
    for i in range(tot):
        leftplan = 0
        rightplan = 0
        if left > 0:
            esl = (s + x) * p
            etl = (t - a) * q
            leftplan = min(esl, etl)
        if right > 0:
            esr = (s - b) * p
            etr = (t + y) * q
            rightplan = min(esr, etr)
        if leftplan > rightplan:
            choice = leftplan
            left -= 1
            s, t = s + x, t - a
            ansleft = min(ansleft, leftplan)
        else:
            choice = rightplan
            right -= 1
            s, t = s - b, t + y
            ansright = min(ansright, rightplan)
        # print("leftplan =", leftplan, "\trightplan =", rightplan, "\ts =", s, "\tt =", t)
        # print("ansleft =", ansleft, "\tansright =", ansright)
    ans = -1-(ansleft + ansright)
    assert ans == work(p,q)
    return ans

import sympy


def work(p, q):
    ans = p * q - p - q
    return ans


# -- author: lijw --
if __name__ == '__main__':
    # p = 11
    # q = sympy.nextprime(p)
    # for i in range(100):
    #     print("p =", p, "\tq =", q, "\tans =", test(p, q)-(p-1)*(q-1), "\t(q-p)//2-2 =", (q-p)//2-2)
    #     # p = sympy.nextprime(p)
    #     q = sympy.nextprime(q)

    T = int(input())
    for _ in range(T):
        p, q = map(int, input().split(' '))
        print(work(p, q))

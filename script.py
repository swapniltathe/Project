from math import gcd
_t_ = int(input())
if 1 <= _t_ <= 15:
    for t in range(_t_):
        n, a, b, k = map(int, input().split())
        if 1 <= k <= n <= 1000000000000000000:
            if 1 <= a <= 1000000000 and 1 <= b <= 1000000000:
                u = (a * b) / gcd(a, b)
                appy = n//a
                chef = n//b
                comn = n//u
                if (appy + chef) - (2 * comn) >= k:
                    print("Win")
                else:
                    print("Lose")

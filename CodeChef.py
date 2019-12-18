# https://www.codechef.com/DEC19B/problems/WATSCORE - AC
from functools import reduce
_t_ = int(input())
if 1 <= _t_ <= 10:
    for t in range(_t_):
        sdic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        _n_ = int(input())
        if 1 <= _n_ <= 1000:
            for n in range(_n_):
                sub, marks = map(int, input().split())
                if 1 <= sub <= 11 and 0 <= marks <= 100:
                    if sub in sdic.keys() and sdic[sub] < marks:
                        sdic[sub] = marks
            print(reduce(lambda x, y: x + y, sdic.values()))
##################
# https://www.codechef.com/problems/SNCKYEAR - Partial
hosted = [2010, 2015, 2016, 2017, 2019]
_t_ = int(input())
if 1 <= _t_ <= 10:
    for t in range(_t_):
        n = int(input())
        if 2010 <= n <= 2019:
            if n in hosted:
                print("HOSTED")
            else:
                print("NOT HOSTED")
###################
# https://www.codechef.com/problems/TLG
# try:
#     n=int(input())
#     arr=[[],[]]
#     sum1=0
#     sum2=0
#     for i in range(n):
#         a,b=map(int,input().split(' '))
#         sum1+=a
#         sum2+=b
#         if sum1>sum2:
#             arr[0].append(1)
#             arr[1].append(sum1-sum2)
#         else:
#             arr[0].append(2)
#             arr[1].append(sum2-sum1)
#     m=max(arr[1])
#     i=arr[1].index(m)
#     j=arr[0][i]
#     print(j,end=" ")
#     print(m)
# except EOFError:
#     pass

# My program:
try:
    l_dict = {1: 0, 2: 0}
    sum1 = 0
    sum2 = 0
    for __ in range(int(input())):
        f, s = map(int, input().split())
        sum1 += f
        sum2 += s
        if sum1 > sum2:
            l = sum1 - sum2
            if l_dict[1] < l:
                l_dict[1] = l
        else:
            l = sum2 - sum1
            if l_dict[2] < l:
                l_dict[2] = l
    if l_dict[1] > l_dict[2]:
        print(1, l_dict[1])
    else:
        print(2, l_dict[2])
except EOFError:
    pass
####################
# https://www.codechef.com/DEC19B/problems/BINADD - Partial
def add(a, b):
    loop = 0
    while b > 0:
        u = a ^ b
        v = a & b
        a = u
        b = v * 2
        loop += 1
    return loop


for __ in range(int(input())):
    num1 = int(input(), 2)
    num2 = int(input(), 2)
    if 1 <= num1 <= 100000 and 1 <= num2 <= 100000:
        print(add(num1, num2))
    else:
        pass
##############################
## From Home PC codechef.py ##
##############################
# Calendar https://www.codechef.com/problems/FLOW015
import calendar
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def get_day():
    n = int(input())
    t = calendar.weekday(n, 1, 1)
    print(days[t])


for __ in range(int(input())):
    get_day()
############################################
# ATM https://www.codechef.com/problems/HS08TEST
withdraw, balance = input().split()
withdraw = int(withdraw)
balance = float(balance)
print("%.2f" % (balance - withdraw - .50)) if withdraw % 5 == 0 and withdraw <= (balance - .50) else print("%.2f" % balance)
############################################
# https://www.codechef.com/problems/HMAPPY2
from math import gcd
# for __ in range(int(input())):
#     n, a, b, k = map(int, input().split())
#     # n, a, b, k = input().split()
#     # n = int(n)
#     # a = int(a)
#     # b = int(b)
#     # k = int(k)
#     succ = 0
#     for i in range(1, n + 1):
#         if i % a == 0 and i % b == 0:
#             continue
#         elif i % a == 0 or i % b == 0:
#             succ += 1
#     if succ >= k:
#         print("Win")
#     else:
#         print("Lose")
for __ in range(int(input())):
    n, a, b, k = map(int, input().split())
    u = (a * b) / gcd(a, b)
    appy = n//a
    chef = n//b
    comn = n//u
    if (appy + chef) - (2 * comn) >= k:
        print("Win")
    else:
        print("Lose")
############################################
# https://www.codechef.com/problems/INTEST
rep_lines, div = map(int, input().split())
out = 0
for __ in range(rep_lines):
    if int(input()) % div == 0:
        out += 1
print(out)
############################################
# https://www.codechef.com/DEC19B/problems/PLMU
### WA
for __ in range(int(input())):
    totl_prs = 0
    two = 0
    zero = 0
    n = int(input())
    lst = list(map(int, input().split()))
    if n == len(lst):
        for i in range(len(lst)):
            if lst[i] == 2:
                two += 1
            elif lst[i] == 0:
                zero += 1
            else:
                continue
        two = two // 2
        zero = zero // 2
        totl_prs = two + zero
    else:
        continue
    print(totl_prs)
# Correct code:
try:
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        l = [int(i) for i in input().split()]
        z, tw = 0, 0
        for i in l:
            if i == 0:
                z += 1
            if i == 2:
                tw += 1
        print(((z*(z-1))//2)+((tw*(tw-1))//2))
except:
    pass
############################################
# https://www.codechef.com/problems/FLOW001
for __ in range(int(input())):
    a, b = map(int, input().split())
    print(a + b)
############################################
# https://www.codechef.com/problems/FCTRL2 - Factorial function recursion
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


for __ in range(int(input())):
    print(fact(int(input())))
############################################
# https://www.codechef.com/problems/FLOW006
from functools import reduce
for __ in range(int(input())):
    lst = list(map(int, input()))
    print(reduce(lambda x, y: x + y, lst))
############################################
# https://www.codechef.com/problems/TSORT
lst = []
for __ in range(int(input())):
    lst.append(int(input()))
lst.sort()
for i in lst:
    print(i)
############################################
# https://www.codechef.com/problems/FLOW002
for __ in range(int(input())):
    a, b = map(int, input().split())
    print(a % b)
############################################
# https://www.codechef.com/problems/FLOW004
for __ in range(int(input())):
    num = input()
    num1 = int(num[0])
    num2 = int(num[-1])
    print(num1 + num2)
############################################
# https://www.codechef.com/problems/LUCKFOUR
for __ in range(int(input())):
    num = input()
    count = 0
    for i in num:
        if i == "4":
            count += 1
        else:
            continue
    print(count)
# OR
for __ in range(int(input())):
    num = [int(x) for x in input()]  # Create integer list from input
    cnt = 0
    for i in num:
        if i == 4:
            cnt += 1
    print(cnt)
############################################
# https://www.codechef.com/problems/FLOW007
for __ in range(int(input())):
    num = input()
    rev_num = ""
    for i in range(len(num)-1, -1, -1):
        rev_num += num[i]
    print(int(rev_num))
############################################
# https://www.codechef.com/problems/FSQRT
from math import sqrt
for __ in range(int(input())):
    print(int(sqrt(int(input()))))
############################################
# https://www.codechef.com/problems/CIELRCPT
lst = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
for __ in range(int(input())):
    num = int(input())
    cnt = 0
    while num != 0:
        for j in lst:
            if num - j >= 0:
                num -= j
                cnt += 1
                break
    print(cnt)
############################################
# https://www.codechef.com/DEC19B/problems/BINXOR
from itertools import permutations
# a = [1, 2, 3]
# prod = permutations(a)
# print(list(prod))
#
# def tostring(lst):
#     return ''.join(lst)
#
#
# def permute(a, l, r):
#     if l == r:
#         b_perm.append(tostring(a))
#         # print(tostring(a))
#     else:
#         for i in range(l, r+1):
#             a[l], a[i] = a[i], a[l]
#             permute(a, l+1, r)
#             a[l], a[i] = a[i], a[l]
for __ in range(int(input())):
    n = int(input())
    a = [int(_, 2) for _ in input()]
    b = [int(_, 2) for _ in input()]
    a_tup = permutations(a)
    a_perm = set(int(i, 2) for i in [''.join(map(str, j)) for j in a_tup])
    # a_perm = set(''.join(map(str, _)) for _ in a_tup)
    # print(a_perm)
    b_tup = permutations(b)
    b_perm = set(int(i, 2) for i in [''.join(map(str, j)) for j in b_tup])
    # b_perm = set(''.join(map(str, _)) for _ in b_tup)
    # print(b_perm)
    res = []
    # out = []
    if n == len(a) and n == len(b):
        # print(a, b)
        # permute(a, 0, n-1)
        # a_perm = b_perm.copy()
        # b_perm.clear()
        # permute(b, 0, n-1)
        # print(a_perm)
        # print(b_perm)
        for i in a_perm:
            for j in b_perm:
                res.append((i ^ j) % 2)
        print(len(set(res)))
#
# lst = [(1, 0), (0, 1)]
# result = [''.join(map(str, i)) for i in lst]
# out = [int(i, 2) for i in result]
# print(out)
# Modulo 1000000007
1
1000
1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# Correct code
m = 1000000007
f = [1]
p = 1
for i in range(2, 100000):
    f.append(p)
    p = (p*i) % m
t = int(input())
for x in range(t):
    n = int(input())
    a = input()
    b = input()
    s = 0
    o1 = 0
    o2 = 0
    for y in range(n):
        if a[y] == '1':
            o1 = o1+1
        if b[y] == '1':
            o2 = o2+1
    st = abs(o1-o2)
    if o1 < o2:
        o1 = o2
    en = min(o1-st, n-o1)*2
    en = en+st
    c = 1
    e = 0
    for y in range(st, en+1, 2):
        b1 = int(pow(f[y], m-2, m))
        b2 = int(pow(f[n-y], m-2, m))
        #c = (c*(n-y+1))%m
        #c = (c*b1)%m
        c = (f[n]*b1*b2) % m
        s = (s+c) % m
    print(s)
############################################

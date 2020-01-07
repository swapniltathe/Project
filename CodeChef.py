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
        two = (two * (two-1)) // 2
        zero = (zero * (zero-1)) // 2
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
# https://www.codechef.com/problems/CMPRSS
try:
    for _ in range(int(input())):
        n = int(input())
        lst = list(map(int, input().split()))
        lst.append(0)
        c = 0
        for i in range(n):
            if lst[i+1] - lst[i] == 1:
                c += 1
            else:
                if i != n-1:
                    if c >= 2:
                        print("{}...{},".format(lst[i-c], lst[i]), end='')
                        c = 0
                    elif c == 1:
                        print("{},{},".format(lst[i-c], lst[i]), end='')
                        c = 0
                    else:
                        print("{},".format(lst[i]), end='')
                        c = 0
                else:
                    if c >= 2:
                        print("{}...{}".format(lst[i-c], lst[i]))
                        c = 0
                    elif c == 1:
                        print("{},{}".format(lst[i-c], lst[i]))
                        c = 0
                    else:
                        print("{}".format(lst[i]))
                        c = 0
except:
    pass
############################################
# https://www.codechef.com/problems/MXCH
for _ in range(int(input())):
    n, k = map(int, input().split())
    for i in range(k):
        print(i+1, end=" ")
    for j in range(n, k, -1):
        print(j, end=" ")
############################################
# https://www.codechef.com/problems/SC31
def xor(s1, s2):
    y = ''.join('0' if i == j else '1' for i, j in zip(s1, s2))
    return y
t = int(input())
for _ in range(t):
    n = int(input())
    weapons = []
    for _ in range(n):
        weapons.append(input())
    res = weapons[0]
    for i in weapons[1:]:
        res = xor(res, i)
    count = 0
    for i in res:
        if i == '1':
            count += 1
    print(count)
############################################
# https://www.codechef.com/problems/SC31
def xor(x, y):
    z = ''.join('0' if k == l else '1' for k, l in zip(x, y))
    # z = ''
    # for k, l in zip(x, y):
    #     if k == l:
    #         z += '0'
    #     else:
    #         z += '1'
    return z


for _ in range(int(input())):
    lst = []
    for i in range(int(input())):
        lst.append(input())
    res = lst[0]
    for j in lst[1:]:
        res = xor(res, j)
    print(res.count('1'))
############################################
# https://www.codechef.com/problems/HRDSEQ
for _ in range(int(input())):
    n = int(input())
    lst = [0]
    e = 0
    for i in range(n-1):
        s = i
        for j in range(i-1, -1, -1):
            if lst[i] == lst[j]:
                e = j
                break
            else:
                e = i
        lst.append(s-e)
    print(lst.count(lst[n-1]))
############################################
# https://www.codechef.com/problems/CHNGIT
from functools import reduce
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    # lst.sort()
    dic = Counter(lst)
    # dic = {}
    # for i in range(n):
    #     dic[lst[i]] = lst.count(lst[i])
    if len(dic.values()) != 1:
        val = list(dic.values())
        val.sort(reverse=True)
        print(n - val[0])
        # print(reduce(lambda x, y: x+y, val[1:]))
    else:
        print(0)
############################################
# https://www.codechef.com/COOK113B/problems/PRFYIT
for _ in range(int(input())):
    s=input()
    n=len(s)
    #3 parts  0 1 0  or 1 0 1
    pre1=[0]*(n+1)
    maxi=0
    pre0=[0]*(n+1)
    for i in range(1,n+1):
        pre1[i]=pre1[i-1]+(s[i-1]=='1')
        pre0[i]=pre0[i-1]+(s[i-1]=='0')
    for i in range(n):
        for j in range(i,n):
            #010
            case1 =pre0[i]+pre1[j+1]-pre1[i]+pre0[n]-pre0[j]
            #101
            case2 =pre1[i]+pre0[j+1]-pre0[i]+pre1[n]-pre1[j]
            maxi=max(maxi,case1,case2)
    print(n-maxi)
# my version (used PyPy3 to submit)
for _ in range(int(input())):
    S = input()
    n = len(S)
    cnt0 = [0] * (n+1)
    cnt1 = [0] * (n+1)
    for i in range(1, n+1):
        if S[i-1] == '0':
            cnt0[i] = cnt0[i-1] + 1
            cnt1[i] = cnt1[i-1]
        else:
            cnt1[i] = cnt1[i-1] + 1
            cnt0[i] = cnt0[i-1]
    mx = 0
    for j in range(n):
        for k in range(j, n):
            olo = cnt0[j] + cnt1[k+1] - cnt1[j] + cnt0[n] - cnt0[k]
            lol = cnt1[j] + cnt0[k+1] - cnt0[j] + cnt1[n] - cnt1[k]
            mx = max(mx, olo, lol)
    print(n-mx)
############################################
# https://www.codechef.com/JAN20B/problems/BRKBKS
for _ in range(int(input())):
    s, w1, w2, w3 = map(int, input().split())
    if 1 <= w1 <= 2 and 1 <= w2 <= 2 and 1 <= w3 <= 2 and 1 <= s <= 8:
        # non-reverse
        h1 = 0
        o = 0
        if s == w1:
            h1 += 1
        else:
            o = s - w1

        if o != 0:
            if o - w2 == 0:
                h1 += 1
                o = 0
            elif o - w2 < 0:
                h1 += 1
                if s == w2:
                    h1 += 1
                    o = 0
                else:
                    o = s - w2
            else:
                o -= w2
        else:
            if s == w2:
                h1 += 1
            else:
                o = s - w2

        if o != 0:
            if o - w3 == 0:
                h1 += 1
            elif o - w3 < 0:
                h1 += 2
            else:
                h1 += 1
        else:
            h1 += 1

        # reverse
        h2 = 0
        o = 0
        if s == w3:
            h2 += 1
        else:
            o = s - w3

        if o != 0:
            if o - w2 == 0:
                h2 += 1
                o = 0
            elif o - w2 < 0:
                h2 += 1
                if s == w2:
                    h2 += 1
                    o = 0
                else:
                    o = s - w2
            else:
                o -= w2
        else:
            if s == w2:
                h2 += 1
            else:
                o = s - w2

        if o != 0:
            if o - w1 == 0:
                h2 += 1
            elif o - w1 < 0:
                h2 += 2
            else:
                h2 += 1
        else:
            h2 += 1

        print(min(h1, h2))
############################################
# https://www.codechef.com/JAN20B/problems/DYNAMO
for _ in range(int(input())):
    n = int(input())
    a = int(input())
    s = (((10 ** n)*2)+a)
    print(s)
    b = int(input())
    c = (((10 ** n)-1)-b)+1
    print(c)
    d = int(input())
    e = (((10 ** n)-1)-d)+1
    print(e)
    ans = int(input())
    if ans == 1:
        pass
    else:
        exit(1)
############################################
# https://www.codechef.com/JAN20B/problems/ANTHILL
from itertools import permutations as perm
n, m, a, r = map(int, input().split())
k_lst = list(range(1, n+1))
# print(k_lst)
k = list(perm(k_lst, 2))
print(k)
############################################

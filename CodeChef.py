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
####################

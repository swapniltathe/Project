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
#
#
# for __ in range(int(input())):
#     n = int(input())
#     a = [_ for _ in input()]
#     b = [_ for _ in input()]
#     a_perm = []
#     b_perm = []
#     res = []
#     out = []
#     if n == len(a) and n == len(b):
#         # print(a, b)
#         permute(a, 0, n-1)
#         a_perm = b_perm.copy()
#         b_perm.clear()
#         permute(b, 0, n-1)
#         # print(a_perm)
#         # print(b_perm)
#         for m in (int(m, 2) for m in a_perm):
#             for j in (int(j, 2) for j in b_perm):
#                 res.append(m ^ j)
#         print(len(set(res)))
for i in range(1001):
    print("0", end="")

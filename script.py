for __ in range(int(input())):
    n = int(input())
    lst = list(int(_) for _ in input().split())
    nlst = [lst[0]]
    out = []
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]-1:
            nlst.append(lst[i+1])
        else:
            if nlst:
                if len(nlst) > 2:
                    out.extend((nlst[0], "...", nlst[-1]))
                else:
                    out.extend((nlst[0], nlst[1]))
            nlst.clear()
            out.append(lst[i+1])
    if nlst:
        if len(nlst) > 2:
            out.extend((nlst[0], "...", nlst[-1]))
        else:
            out.extend(nlst)
    else:
        out.append(lst[i])
    print(''.join(out))

# 1 2 3 4 5
#
# loop 1 to 5
# check 1 = (2-1)
#     True: nlst = 1, 2
#     false:
#         if nlst has value:
#             if nlist values greater than 2:
#                   str += nlst[0],"...", nlst[-1]
#             else
#                   str += nlist[0], nlist[1]
#         nlst = blank
#         str += 1,

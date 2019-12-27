# https://www.codechef.com/COOK113B/problems/PRFYIT
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

for _ in range(int(input())):
    l = [100, 50, 10, 5, 2, 1]
    n = int(input())
    count = 0
    while n > 0:
        for i in l:
            if n - i >= 0:
                count += 1
                n -= i
                break
    print(count)

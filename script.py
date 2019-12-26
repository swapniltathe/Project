try:
    ic = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8), (0, 3), (3, 6), (1, 4), (4, 7), (2, 5), (5, 8)]
    board = [(1, 2, 3, 4, 5, 6, 7, 8, 9)]
    boardfq = {(1, 2, 3, 4, 5, 6, 7, 8, 9): 0}

    for state in board:
        for present in [(a, b) for a, b in ic if (state[a] + state[b]) in [2, 3, 5, 7, 11, 13, 17]]:
            new_ic = list(state[:])
            new_ic[present[0]], new_ic[present[1]] = new_ic[present[1]], new_ic[present[0]]
            new_ic = tuple(new_ic)
            if new_ic not in boardfq:
                boardfq[new_ic] = boardfq[state] + 1
                board.append(new_ic)

    for _ in range(int(input())):
        i = tuple([int(x) for x in ' '.join([input().strip() for _ in range(4)]).split(' ') if x != ''])
        if i in boardfq:
            print(boardfq[i])
        else:
            print(-1)
except:
    pass
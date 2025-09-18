def checkmate(board_string):
    board = [list(row) for row in board_string.strip().splitlines()]
    size = len(board)

    count_K = 0
    count_Q = 0
    count_R = 0
    count_B = 0
    count_P = 0

    for row in board:
        for item in row:
            if item == 'K':
                count_K += 1
            elif item == 'Q':
                count_Q += 1
            elif item == 'R':
                count_R += 1
            elif item == 'B':
                count_B += 1
            elif item == 'P':
                count_P += 1

    if count_K > 1 or count_Q > 1 or count_R > 2 or count_B > 2 or count_P > 8:
        print("Error")
        return

    kPosition = None
    for t in range(size):
        for s in range(size):
            if board[t][s] == 'K':
                kPosition = (t, s)
                break
        if kPosition:
            break

    if not kPosition:
        return 

    kt, ks = kPosition

    directions = {
        'rook': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'bishop': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'pawn': [(-1, -1), (-1, 1)]
    }

    def case(t, s):
        return 0 <= t < size and 0 <= s < size

    for dt, ds in directions['pawn']:
        nt, ns = kt + dt, ks + ds
        if case(nt, ns) and board[nt][ns] == 'P':
            print("Success")
            return

    for dt, ds in directions['bishop']:
        nt, ns = kt + dt, ks + ds
        while case(nt, ns):
            item = board[nt][ns]
            if item != '.':
                if item in ['B', 'Q']:
                    print("Success")
                    return
                break
            nt += dt
            ns += ds

    for dt, ds in directions['rook']:
        nt, ns = kt + dt, ks + ds
        while case(nt, ns):
            item = board[nt][ns]
            if item != '.':
                if item in ['R', 'Q']:
                    print("Success")
                    return
                break
            nt += dt
            ns += ds

    print("Fail")
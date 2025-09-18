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
    for y in range(size):
        for x in range(size):
            if board[y][x] == 'K':
                kPosition = (y, x)
                break
        if kPosition:
            break

    if not kPosition:
        return 

    ky, kx = kPosition

    directions = {
        'rook': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'bishop': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'pawn': [(-1, -1), (-1, 1)]
    }

    def case(y, x):
        return 0 <= y < size and 0 <= x < size

    for dy, dx in directions['pawn']:
        ny, nx = ky + dy, kx + dx
        if case(ny, nx) and board[ny][nx] == 'P':
            print("Success")
            return

    for dy, dx in directions['bishop']:
        ny, nx = ky + dy, kx + dx
        while case(ny, nx):
            item = board[ny][nx]
            if item != '.':
                if item in ['B', 'Q']:
                    print("Success")
                    return
                break
            ny += dy
            nx += dx

    for dy, dx in directions['rook']:
        ny, nx = ky + dy, kx + dx
        while case(ny, nx):
            item = board[ny][nx]
            if item != '.':
                if item in ['R', 'Q']:
                    print("Success")
                    return
                break
            ny += dy
            nx += dx

    print("Fail")
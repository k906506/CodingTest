def solution(board, aloc, bloc):
    row = len(board)
    col = len(board[0])

    if row * col == 1 or row * col == 2:
        return 0
    else:
        queue = []
        aVisit = [[0 for i in range(col)] for i in range(row)]
        bVisit = [[0 for i in range(col)] for i in range(row)]

        host = [(aloc[0], aloc[1]), (bloc[0], bloc[1])]

        queue.append(aloc)
        while queue:
            y, x = queue.pop(0)
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < col and ny >= 0 and ny < row and board[ny][nx] == 1 and aVisit[ny][nx] == 0:
                    aVisit[ny][nx] += aVisit[y][x] + 1
                    queue.append((ny, nx))

        queue = []
        queue.append(bloc)
        while queue:
            y, x = queue.pop(0)
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < col and ny >= 0 and ny < row and board[ny][nx] == 1 and bVisit[ny][nx] == 0:
                    bVisit[ny][nx] += bVisit[y][x] + 1
                    queue.append((ny, nx))

        for i in range(row):
            for j in range(col):
                aVisit[i][j] += bVisit[i][j]

        max = -1
        min = 1e9
        for i in range(row):
            for j in range(col):
                if (i, j) not in host:
                    if aVisit[i][j] > max:
                        max = aVisit[i][j]
                    if aVisit[i][j] < min:
                        min = aVisit[i][j]

        if max == min:
            return max
        else:
            if max == 0:
                return 0
            elif min == 0:
                return max
            else:
                return max + min - 1
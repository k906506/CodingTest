def solution(board, skill):
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:  # 적의 공격
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    board[i][j] -= degree
        else:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    board[i][j] += degree

    cnt = 0
    for row in board:
        for col in row:
            if col >= 1:
                cnt += 1

    return cnt

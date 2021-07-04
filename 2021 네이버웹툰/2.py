def solution(grid):
    h = len(grid)
    w = len(grid[0])

    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = grid[0][0]

    dx = [-1, 0]
    dy = [0, -1]

    for i in range(h):
        for j in range(w):
            mid = []
            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < h and 0 <= ny < w:
                    mid.append(dp[nx][ny])
            if mid:
                dp[i][j] = grid[i][j] + min(mid)
            else:
                dp[i][j] = grid[i][j]

    return dp[h - 1][w - 1]

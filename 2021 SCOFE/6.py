def main():
    n, m = map(int, input().split()) # 가로, 세로
    store = [[] for _ in range(m)]
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        store[i] = list(map(int, input().split()))

    dp[0][0] = store[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + store[0][i]

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[i][j] = dp[i-1][j] + store[i][j]
            else:
                dp[i][j] = max(dp[i][j - 1] + store[i][j], dp[i - 1][j] + store[i][j])

    print(max(max(dp)))

if __name__ == "__main__":
    main()
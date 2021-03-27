def main():
    n = int(input())
    line = input()

    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 1

    for i in range(1, len(line)):
        if line[i] == "0":
            dp[i+1] = dp[i]
        else:
            dp[i+1] = dp[i] + dp[i-1]

    print(dp)
    print(max(dp))

if __name__ == "__main__":
    main()
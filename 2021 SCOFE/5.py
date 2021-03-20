INF = float('inf')

def main():
    i, j = map(int, input().split()) # 가로, 세로
    data = [[] for _ in range(j)]

    for x in range(j):
        data[x] = list(input())

    src = list()
    for x in range(j):
        for y in range(i):
            if data[x][y] == "c":
                src.append((x, y))

    final = []
    for src_x, src_y in src:
        result = [[-1 for _ in range(i)] for _ in range(j)]
        ans = bfs(data, result, src_x, src_y, i, j)

        check = False
        for k in range(i):
            if ans[j-1][k] != -1:
                check = True
            else:
                ans[j-1][k] = INF

        if check:
            final.append(min(ans[j-1]))

    if len(final) != 0:
        print(min(final))
    else:
        print(-1)

def bfs(data, result, src_x, src_y, i, j):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    result[src_x][src_y] = 0

    queue = []
    queue.append([src_x, src_y])

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and nx < j and ny >= 0 and ny < i:
                if data[nx][ny] == "." and result[nx][ny] == -1:
                    queue.append([nx, ny])
                    if ny != y and nx == x:
                        result[nx][ny] = result[x][y] + 1
                    elif ny == y and nx != x:
                        result[nx][ny] = result[x][y]

    return result

if __name__ == "__main__":
    main()
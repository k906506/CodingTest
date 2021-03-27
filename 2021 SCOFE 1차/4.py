def main():
    score = list(map(float, input().split()))
    n, m = map(int, input().split())

    like = [[] for _ in range(n)]
    genre = [[] for _ in range(n)]

    for i in range(n):
        like[i] = list(input())

    for i in range(n):
        genre[i] = list(input())

    result = dict()
    content = list()

    for i in range(n):
        for j in range(m):
            if like[i][j] != "W":
                if genre[i][j] not in result:
                    result[genre[i][j]] = []
                if genre[i][j] not in content:
                    content.append(genre[i][j])

    for i in range(n):
        for j in range(m):
            if like[i][j] != "W":
                if like[i][j] == "Y":
                    result[genre[i][j]].append(((i, j), 1))
                else:
                    result[genre[i][j]].append(((i, j), 0))

    for element in content:
        result[element] = sorted(result[element], key = lambda x : (-x[1], x[0][1], x[0][0]))
        result[element].append(score[ord(element)-65])

    print(result)

if __name__ == "__main__":
    main()
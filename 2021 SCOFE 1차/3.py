def main():
    n = int(input())
    room = [[] for _ in range(n)]
    result = [0 for _ in range(n)]

    for i in range(n):
        room[i] = list(map(int, input()))

    for size in range(1, n):
        for i in range(n - size + 1):
            for j in range(n - size + 1):
                if check_room(room, size, i, j):
                    result[size] += 1

    print("total: %d" %sum(result))
    for i in range(len(result)):
        if result[i] != 0:
            print("size[%d]: %d" %(i, result[i]))

def check_room(room, size, src_x, src_y):
    check = True
    for i in range(src_x, src_x + size):
        for j in range(src_y, src_y + size):
            if room[i][j] == 0:
                check = False
    return check

if __name__ == "__main__":
    main()
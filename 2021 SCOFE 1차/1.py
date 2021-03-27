def main():
    n = int(input())
    time = list()

    for i in range(n):
        time_input = input().rstrip()
        src = int(time_input[:2] + time_input[3:5])
        dst = int(time_input[8:10] + time_input[11:])
        time.append((src, dst))

    time = sorted(time, key = lambda x : (x[0], -x[1]))

    src_max = time[0][0]
    dst_min = time[0][1]

    check = True

    for i in range(1, len(time)):
        if time[i][0] >= src_max and time[i][0] <= dst_min:
            src_max = time[i][0]
        else:
            check = False
        if dst_min >= time[i][1]:
            dst_min = time[i][1]

    if check:
        src_max = str(src_max)
        dst_min = str(dst_min)
        print("%s:%s ~ %s:%s" %(src_max[:2], src_max[2:], dst_min[:2], dst_min[2:]))
    else:
        print(-1)

if __name__ == '__main__':
    main()
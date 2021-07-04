def solution(lottery):
    result = dict()

    for i, j in lottery:
        if result.get(i) == None:
            result[i] = [0, 0]
        if j == 0:  # 미당첨
            if result[i][1] == 0:  # 아직 미당첨인 경우
                result[i][0] += 1
        else:
            if result[i][1] == 0:  # 첫 번째 당첨인 경우
                result[i][0] += 1
                result[i][1] = 1

    sum = 0
    cnt = 0
    for e in result:
        if result[e][1] == 1:
            cnt += 1
            sum += result[e][0]

    if cnt == 0:
        return 0

    return sum // cnt
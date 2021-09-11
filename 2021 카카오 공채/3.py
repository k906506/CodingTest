def solution(fees, records):  # 기본 시간, 기본 요금, 단위 시간, 단위 요금

    # 어차피 순서대로 들어옴
    history = {}
    result = []
    for e in records:
        time, number, kind = e.split(" ")
        if history.get(number) == None:
            history[number] = []
            history[number].append(time)
        else:
            history[number].append(time)

    for e in history:
        checkIn = True
        resultHour = 0
        resultMinute = 0
        for time in history[e]:
            if checkIn:  # 들어온 경우
                checkInHour, checkInMinute = map(int, time.split(":"))
                checkIn = False
            else:
                checkOutHour, checkOutMinute = map(int, time.split(":"))
                resultHour += checkOutHour - checkInHour
                resultMinute += checkOutMinute - checkInMinute
                if resultMinute < 0:
                    resultHour -= 1
                    resultMinute = 60 + resultMinute
                checkIn = True
        if not checkIn:  # 들어왔지만 나가지 않은 경우
            resultHour += 23 - checkInHour
            resultMinute += 59 - checkInMinute
            if resultMinute < 0:
                resultHour -= 1
                resultMinute = 60 + resultMinute
        result.append((e, resultHour * 60 + resultMinute))

    result = sorted(result, key=lambda x: x[0])
    answer = []
    for e in result:
        total = e[1]
        ans = 0
        if total <= fees[0]:
            ans += fees[1]
        else:
            temp = (total - fees[0]) % fees[2]
            if temp != 0:  # 반올림
                ans += fees[1] + (((total - fees[0]) // fees[2]) + 1) * fees[3]
            else:
                ans += fees[1] + ((total - fees[0]) // fees[2]) * fees[3]
        answer.append(ans)

    return answer

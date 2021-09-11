def solution(n, k):
    change = ""
    while n >= k:  # 이때만 실행
        temp = n // k
        n1 = n - temp * k  # 나머지
        n = temp
        change += str(n1)
    change += str(n)
    change = change[::-1]

    change = change.replace("0", " ").split(" ")

    result = []
    for e in change:
        if e != "1" and e != "":
            result.append(e)

    for e in result:
        e = int(e)
        if e != 2 and e % 2 == 0:
            result.remove(str(e))
        elif e != 3 and e % 3 == 0:
            result.remove(str(e))
        elif e != 5 and e % 5 == 0:
            result.remove(str(e))
        elif e != 7 and e % 7 == 0:
            result.remove(str(e))
        elif e != 11 and e % 11 == 0:
            result.remove(str(e))
        elif e != 53 and e % 53 == 0:
            result.remove(str(e))

    return len(result)

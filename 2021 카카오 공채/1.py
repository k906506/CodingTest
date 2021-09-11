def solution(id_list, report, k):
    report = set(report)
    report = list(report)

    history = {}
    count = {}
    for e in id_list:
        history[e] = []
        count[e] = 0

    for e in report:
        a, b = e.split(" ")
        history[a].append(b)
        count[b] += 1

    send = []
    for e in count:
        if count[e] >= k:
            send.append(e)

    answer = []
    for e in history:
        cnt = 0
        for element in send:
            if element in history[e]:
                cnt += 1
        answer.append(cnt)

    return answer

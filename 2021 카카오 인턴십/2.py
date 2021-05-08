def find(index, room):
    person = []
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'P':
                person.append((i, j))
                continue
    
    for i in range(len(person)):
        for j in range(i+1, len(person)):
            dist = abs(person[i][0] - person[j][0]) + abs(person[i][1] - person[j][1])
            if dist <= 1:
                return 0
            
            elif dist == 2:
                if person[i][0] == person[j][0]:
                    x = person[i][0]
                    y = (person[i][1] + person[j][1])//2
                    if room[x][y] != 'X':
                        return 0
                elif person[i][1] == person[j][1]:
                    x = (person[i][0] + person[j][0])//2
                    y = person[i][1]
                    if room[x][y] != 'X':
                        return 0
                else:
                    check = []
                    check.append((person[i][0], person[j][1]))
                    check.append((person[j][0], person[i][1]))
                    for i in range(2):
                        if room[check[i][0]][check[i][1]] != 'X':
                            return 0
                
    return 1
    
def solution(places):
    answer = []
    for i in range(5):
        answer.append(find(i, places[i]))
    
    return answer

INF = float('inf')

import heapq

def djikstra(world, worldLink, src):
    heap = []
    distance = dict()
    visit = dict()

    for i in range(len(world)):
        distance[world[i]] = INF
        visit[world[i]] = False
    
    distance[src] = 0
    heapq.heappush(heap, [0, src])

    while heap:
        current_node = heapq.heappop(heap)
        if visit[current_node[1]] == True:
            continue

        for element in worldLink[current_node[1]]:
            if distance[current_node[1]] + element[1] < distance[element[0]]:
                distance[element[0]] = distance[current_node[1]] + element[1]
                heapq.heappush(heap, [distance[element[0]], element[0]])

        visit[current_node[1]] = True

    ans = 0
    for element in world:
        ans += distance[element]
    
    return ans

def main():
    n = int(input())

    worldLink = dict()
    world = list()
    for _ in range(n):
        src, dst, distance = input().split()
        distance = int(distance)
        if src not in world:
            world.append(src)
            worldLink[src] = []
        if dst not in world:
            world.append(dst)
            worldLink[dst] = []
        worldLink[src].append((dst, distance))
    
    result = INF
    for element in world:
        ans = djikstra(world, worldLink, element)
        if ans != 0:
            result = min(result, ans)
    
    print(result)
    
if __name__ == "__main__":
    main()
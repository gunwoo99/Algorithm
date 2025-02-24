import heapq

N = 1
S = 1
E = [[] for _ in range(N)]

def prim():
    queue = []
    heapq.heappush(queue, (0, S))
    
    visited = [False for _ in range(N)]
    distance = [float("inf") for _ in range(N)]
    
    num = 0
    MST = 0
    while num != N and queue:
        c, u = heapq.heappop(queue)
        if visited[u]:
            continue
        
        visited[u] = True
        MST += c
        num += 1
        for v in E[u]:
            if visited[v[0]] == False and v[1] < distance[v[0]]:
                heapq.heappush(queue, (v[1], v[0]))
                distance[v[0]] = v[1]
    return MST

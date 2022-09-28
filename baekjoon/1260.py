# 정점 번호가 작은 것을 먼저 방문
N, M, start = map(int, input().split())
graph = {}

for i in range(N):
    graph[i+1] = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N):
    temp = graph[i+1]
    graph[i+1] = sorted(temp, reverse=True)
    

def dfs(graph, start):
    need_visit = []
    visited = [start]
    need_visit.extend(graph[start])

    while need_visit:
        node = need_visit.pop()

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

def bfs(graph, start):
    visited = []
    need_visit = graph[start]
    visited.append(start)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            need_visit = graph[node] + need_visit
            visited.append(node)
    return visited
temp = dfs(graph, start)
print(*temp)
temp = bfs(graph, start)
print(*temp)

# https://www.acmicpc.net/problem/24479

import sys
N, M, start = map(int, sys.stdin.readline().split())
input_list = []
for i in range(M):
    input_list.append(list(map(int, sys.stdin.readline().split())))

graph = {}
for i in range(N):
    graph[i+1] = []
    
for i in input_list:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in graph.keys():
    graph[i] = sorted(graph[i], reverse=True)

visited = [0] * (N+1)
need_visit = []
need_visit.append(start)
cnt = 0
while need_visit:
    node = need_visit.pop()
    if visited[node] == 0:
        cnt += 1
        visited[node] = cnt
        need_visit.extend(graph[node])
for i in visited[1:]:
    print(i)

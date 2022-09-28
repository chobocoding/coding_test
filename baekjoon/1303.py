from copy import deepcopy

answer = [0, 0]
n, m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(input()))

def count_sol(graph, color):
    graph_ = deepcopy(graph)
    matrix = []
    point = 0
    point_list = []
    for i in range(m):
        matrix.append([0]*n)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(m):
        for j in range(n):
            if graph[i][j] != color: continue

            need_visit = [[i,j]]
            point = 0
            while need_visit:
                y, x = need_visit.pop()
                if graph_[y][x] == color:
                    graph_[y][x] = False
                    point += 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if graph_[ny][nx] != color:
                        continue
                    need_visit.append([ny,nx])
            if point == 0: continue
            point_list.append(point)
    return point_list

for i in count_sol(graph, 'W'):
    answer[0] = answer[0] + i**2
for i in count_sol(graph, 'B'):
    answer[1] = answer[1] + i**2
print(*answer)

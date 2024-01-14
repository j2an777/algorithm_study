# 1. 익은 과일이 있는지부터 판단
# 2. 있으면 bfs로 돌아가면서 0에 대해서는 1로 전환

from collections import deque

def bfs() :
    q = deque()
    
    for i in range(row) :
        for j in range(col) :
            if graph[i][j] == 1 :
                q.append([i, j])
    
    while q :
        x, y = q.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    

col, row = map(int, input().split())
graph = []
res = 0
flag = True # 안 익은 과일 유무 판단

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(row) :
    graph.append(list(map(int, input().split())))

bfs()
    
for i in graph :
    for j in i :
        if j == 0 :
            flag = False # 0 발견 시 flag False로 전환
            break
    res = max(res, max(i))
    
if flag == True :
    print(res - 1)
else :
    print(-1)
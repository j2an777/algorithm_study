from collections import deque

def bfs() :
    q = deque()
    
    for i in range(high) :
        for j in range(row) :
            for k in range(col) :
                if graph[i][j][k] == 1 :
                    q.append([i, j, k])
    
    while q :
        # z - high, y - row, x - col로 설정
        z, y, x = q.popleft()
        
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < col and 0 <= ny < row and 0 <= nz < high and graph[nz][ny][nx] == 0 :
                graph[nz][ny][nx] = graph[z][y][x] + 1
                q.append((nz, ny, nx))
    

col, row, high = map(int, input().split())
graph = []
res = 0
flag = True # 안 익은 과일 유무 판단

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(high) :
    layer = []
    for i in range(row) :
        layer.append(list(map(int, input().split())))
    graph.append(layer)
    
bfs()
    
for i in range(high) :
    for j in range(row) :
        for k in range(col) :
            if graph[i][j][k] == 0 :
                flag = False # 0 발견 시 flag False로 전환
                break
            else :
                if graph[i][j][k] > res :
                    res = graph[i][j][k]
        
if flag == True :
    print(res - 1)
else :
    print(-1)
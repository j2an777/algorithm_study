from collections import deque

def bfs(stX, stY) :
    q = deque()
    q.append([stX, stY])
    visited[stX][stY] = True
    
    while q :
        x, y = q.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1 :
                visited[nx][ny] = True
                q.append([nx, ny])
    
t = int(input())

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(t) :
    m, n, k = map(int, input().split())
    
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for j in range(k) :
        x, y = map(int, input().split())
        graph[y][x] = 1
        
    cnt = 0
    
    for i in range(n) :
        for j in range(m) :
            if not visited[i][j] and graph[i][j] == 1 :
                bfs(i, j)
                cnt += 1
    print(cnt)
    
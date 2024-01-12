from collections import deque

def bfs(x, y, rx, ry) :
        
    q = deque()
    q.append((x, y))
    graph[x][y] = 1;
    
    while q :
        x, y = q.popleft()
            
        if x == rx and y == ry :
            return graph[x][y] - 1
        
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < k and 0 <= ny < k and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
            
n = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for i in range(n) :
    k = int(input())
    st, en = map(int, input().split())
    resX, resY = map(int, input().split())
    graph = [[0] * k for _ in range(k)]
    
    print(bfs(st, en, resX, resY))
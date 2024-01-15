from collections import deque

def bfs(x, y, flag) :
    q = deque()
    q.append([x, y])
    
    if flag == 1 :
        visited1[x][y] = True
        
        while q :
            stX, stY = q.popleft()
            
            for i in range(4) :
                nx = stX + dx[i]
                ny = stY + dy[i]
            
                # (x,y) 와 (nx, ny)가 같을 때에만 True
                if 0 <= nx < n and 0 <= ny < n and not visited1[nx][ny] and graph[nx][ny] == graph[x][y] :
                    visited1[nx][ny] = True
                    q.append([nx, ny])
    
    else :
        visited2[x][y] = True
    
        while q :
            stX, stY = q.popleft()
        
            for i in range(4) :
                nx = stX + dx[i]
                ny = stY + dy[i]
            
                if 0 <= nx < n and 0 <= ny < n and not visited2[nx][ny]:
                    if (graph[nx][ny] == 'R' or graph[nx][ny] == 'G') and (graph[x][y] == 'R' or graph[x][y] == 'G'):
                        visited2[nx][ny] = True
                        q.append([nx, ny])
                    
                    elif graph[nx][ny] == 'B' and graph[x][y] == 'B':
                        visited2[nx][ny] = True
                        q.append([nx, ny])
    

n = int(input())

graph = []
for i in range(n) :
    graph.append(list(input()))
    
noeye = 0
eye = 0
    
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 적록색약이 아닌 경우
for i in range(n) :
    for j in range(n) :
        if not visited1[i][j] :
            bfs(i, j, 1)
            noeye += 1
            
# 적록색약인 경우
for i in range(n) :
    for j in range(n) :
        if not visited2[i][j] :
            bfs(i, j, 0)
            eye += 1
            
print(noeye, eye)
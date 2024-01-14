from collections import deque

def bfs(x, y) :
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    
    while q :
        x, y = q.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                           
                
n, m = map(int, input().split())
graph = []

# n 만큼 graph 입력 값 생성
for i in range(n) :
    graph.append(list(map(int, input())))

# q가 다음 방향으로 갈 방향키
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# (0, 0)에서 bfs 호출
bfs(0, 0)

# bfs로 마지막 탐색한 자리에 대한 값 출력
print(graph[n-1][m-1])
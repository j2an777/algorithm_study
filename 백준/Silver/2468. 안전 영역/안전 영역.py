# 1. 입력한 그래프 값들 중 최댓값 저장
# 2. 최댓값 기준으로 반복문으로 1부터 비교할 높이값 지정
# 3. 2중 반복문으로 그래프 각 인덱스 당 높이 비교와 방문 여부 판단
# 4. 크면서 방문 안했을 시 bfs로 다음 노드 방문, 

from collections import deque

def bfs(x, y, h) :
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h :
                visited[nx][ny] = True
                q.append((nx, ny))
    
    
n = int(input())
graph = []
max_value = 0

res = 1

for i in range(n) :
    graph.append(list(map(int, input().split())))
    max_value = max(max_value, max(graph[i]))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for h in range(1, max_value + 1) :
    # 기준 높이 값이 변경될 때마다 초기화
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] > h and not visited[i][j] :
                bfs(i, j, h)
                cnt += 1
                
    # 카운트 최댓값 비교 후 업데이트
    res = max(res, cnt)

print(res)
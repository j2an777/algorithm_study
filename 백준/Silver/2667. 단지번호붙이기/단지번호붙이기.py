# 1. 1인 칸과 방문하지 않은 칸 발견시 dfs호출
# 2. dfs 재귀로 주변 1이 없을때까지 방문하며 카운트
# 3. 끝나면 해당 카운트 리턴 후 배열에 저장
# 4. 배열 값들 오름차순 저장 후 길이와 함께 출력

# 조건 1. 범위 내에만 돌아가도록 범위 조건문 지정

def dfs(x, y) :
    global cnt
    visited[x][y] = True
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1 :
            cnt += 1
            dfs(nx, ny)
            
    return cnt


n = int(input())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

visited = [[False for _ in range(n)] for _ in range(n)]
res = [] # 각 단지 집의 수 배열
cnt = 1  # 집의 수 카운트

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 and not visited[i][j] :
            res.append(dfs(i, j))
            cnt = 1 # cnt 초기화
            
# 집의 수 오름차순
res.sort()

# 단지 개수 출력
print(len(res))

# 각 단지 내 집의 수 출력
for i in res :
    print(i)
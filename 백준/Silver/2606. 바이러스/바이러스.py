def dfs(start_node) :
    visited[start_node] = True
    
    global cnt
    
    for new_node in graph[start_node] :
        if not visited[new_node] : 
            cnt += 1
            # 방문하기 위해 재귀함수 호출
            dfs(new_node)
            
    return cnt

            
n = int(input()) # 컴퓨터의 수
k = int(input()) # 컴퓨터 연결 쌍의 수

# 노드 수 카운트
cnt = 0

# 그래프 생성 (1차원)
graph = []
graph = [[] for _ in range(n + 1)]

# 방문 여부 초기화
visited = [False] * (n + 1)

# 쌍의 수 만큼 연결되어있는 번호 부여
for i in range(k) :
    x, y = map(int, input().split())
    
    # (1, 2)의 경우 간선이니 (2, 1)도 맞기에 입력한 x y에 입력
    graph[x].append(y)
    graph[y].append(x)
    
print(dfs(1))

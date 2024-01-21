def dfs(x, y, box) :
    global res
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 다음 노드의 문자에 대해서 box안의 문자들 중 포함이 되어 있다면 
        if 0 <= nx < r and 0 <= ny < c :
            if graph[nx][ny] not in box :
                dfs(nx, ny, box+graph[nx][ny])
                
    res = max(res, len(box))
                 

r, c = map(int, input().split())

graph = []
res = 0
    
for i in range(r) :
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, 0, graph[0][0])

print(res)
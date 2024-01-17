from collections import deque

def bfs(f, s, g, u, d) :
    q = deque()
    q.append(s)
    graph[s] = 1
    
    while q :
        floor = q.popleft()
        
        if floor == g:
            return graph[floor] - 1
        
        for i in [u, -d] :
            nfloor = floor + i
            
            if 1 <= nfloor <= f and graph[nfloor] == 0 :
                graph[nfloor] = graph[floor] + 1
                q.append(nfloor)
                
    return 'use the stairs'
    
    
f, s, g, u, d = map(int, input().split())
    
graph = [0 for _ in range(f+1)]

res = bfs(f, s, g, u, d)

print(res)
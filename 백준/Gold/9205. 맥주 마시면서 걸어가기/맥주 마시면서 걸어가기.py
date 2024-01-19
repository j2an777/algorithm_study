# 1. 각 지점 간 거리가 1000 넘어가면 안된다.
# 2. 좌표 이동 후 다음 이동해야할 좌표간 거리를 계산한다.
# 3. 남은 맥주로 가능한 거리가 이동간 거리보다 같거나 그 이상인 상황에서 다음 지점으로 이동
# 4. 편의점이면 다시 맥주 개수는 20, 아니라면 간 거리 만큼 소비한 맥주 빼기
# 5. 모든 구간 중 한 구간이라도 짧아서 못 가면 sad 모든 구간이 길어 도착시 happy

from collections import deque

def bfs(start, conv, end) :
    q = deque()
    q.append([start[0], start[1]])
    visited.append([start[0], start[1]])
    
    # 편의점, 도착 지점 저장
    pos = conv + [end]
    
    while q :
        x, y = q.popleft()
        
        # 도착하면 happy 리턴
        if x == end[0] and y == end[1] :
            return 'happy'
        
        # 저장된 지점 이동
        for nx, ny in pos :
            # 지점 간 거리 계산
            dist = abs(nx - x) + abs(ny - y)
            
            # 보유 맥주 개수로 허용 거리가 지점간 거리보다 크다면
            if 1000 >= dist and [nx, ny] not in visited:
                q.append([nx, ny])
                visited.append([nx, ny])
                
    return 'sad'


t = int(input())
res = []

for i in range(t) :
    conNum = int(input())
    start = list(map(int, input().split()))
    conv = [list(map(int, input().split())) for _ in range(conNum)]
    end = list(map(int, input().split()))
    visited = []
    
    res.append(bfs(start, conv, end))
    
for i in res :
    if i == 'happy' :
        print('happy')
    else :
        print('sad')
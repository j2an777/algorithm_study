n, c = map(int, input().split())
x = []

for i in range(n) : 
    x.append(int(input()))
    
x.sort()

# 공유기 간 사이 거리가 1일 때
start = 1
# 공유기 간 사이 거리가 끝과 끝일 때
end = x[-1] - x[0]

res = 0

while start <= end :
    mid = (start + end) // 2
    
    # 시작점에 일단 설치
    wifi = x[0]
    
    # 시작점 설치로 1카운트 시작
    cnt = 1
    
    # 시작 위치
    total = x[0]
    
    for i in range(n) :
        if x[i] - total >= mid :
            total = x[i]
            cnt += 1
        
    if cnt < c :
        end = mid - 1
        
    else :
        res = mid
        start = mid + 1
        
print(res)
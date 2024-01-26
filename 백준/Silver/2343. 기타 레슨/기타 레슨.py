n, m = map(int, input().split())
blueray = list(map(int, input().split()))

# 각 블루레이에 1개씩 담았을 때 (최소)
start = max(blueray)

# 1개의 블루레이에 다 들어갔을 때(최대)
end = sum(blueray)

res = 0

while start <= end :
    mid = (start + end) // 2
    
    total = 0
    cnt = 1
    
    for i in blueray :
        if total + i > mid :
            cnt += 1
            total = 0
            
        total += i
        
    if cnt <= m :
        res = mid
        end = mid - 1
        
    elif cnt > m :
        start = mid + 1
        
print(res)
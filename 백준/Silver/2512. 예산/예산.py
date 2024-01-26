n = int(input())
area = list(map(int, input().split()))
budget = int(input())

start = 0
end = max(area)

res = 0

while start <= end :
    mid = (start + end) // 2
    
    total = 0
    
    for i in area :
        if mid > i :
            total += i
        else :
            total += mid
            
    if total <= budget :
        res = mid
        start = mid + 1
        
    else :
        end = mid - 1
        
print(res)
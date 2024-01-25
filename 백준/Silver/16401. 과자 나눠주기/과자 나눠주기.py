m, n = map(int, input().split())

snack = list(map(int, input().split()))

start = 1
end = max(snack)
res = 0

while start <= end :
    mid = (start + end) // 2
    
    total = 0
    
    for i in snack :
        if i >= mid:
            total += i // mid
    
    if total >= m :
        res = mid
        start = mid + 1
    else :
        end = mid - 1
        
print(res)
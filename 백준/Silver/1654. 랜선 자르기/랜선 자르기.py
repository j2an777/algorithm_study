k, n = map(int, input().split())

line = [int(input()) for _ in range(k)]

res = 0

start = 1

end = sum(line) // n

while start <= end :
    mid = (start + end) // 2
    
    total = 0
    
    for i in line :
        if i >= mid :
            total += i // mid
            
    if total >= n :
        res = mid
        start = mid + 1
        
    else :
        end = mid - 1
        
print(res)
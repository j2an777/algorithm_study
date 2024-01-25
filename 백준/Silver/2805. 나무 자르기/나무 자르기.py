n, m = map(int, input().split())
t = list(map(int, input().split()))

# 나무를 최소한으로는 잘라야 하는 높이
start = 1

# 나무를 최대한으로 자를 수 있는 높이
end = max(t)

res = 0

while start <= end :
    mid = (start + end) // 2
    
    total = 0
    
    for i in t :
        if i - mid >= 0 :
            total += i - mid
                
    if total >= m :
        res = mid
        start = mid + 1
        
    else :
        end = mid - 1
        
print(end)
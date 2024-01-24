n, k = map(int, input().split())
team = []
t = 0

for i in range(n) :
    team.append(int(input()))

team.sort()

start = team[0]
end = team[-1] + k

res = 0

while start <= end :
    mid = (start + end) // 2
    total = 0
    
    for i in team :
        if mid - i >= 0:
            total += mid - i
        
    if total > k :
        end = mid - 1
    
    else :
        start = mid + 1
        res = mid
        
print(res)

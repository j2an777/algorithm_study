n, m = map(int, input().split())
times = []

for i in range(n) :
    times.append(int(input()))
    
# 그냥 가장 빠른 1초를 start로 선정
start = 1

# 가장 오래 걸리는 심사대에만 모든 사람이 심사를 볼 때
end = max(times) * m

res = 0

while start <= end :
    mid = (start + end) // 2
    
    total = 0
    
    # mid에서 각 걸리는 시간에 따른 몫을 구해 심사대 통과하는 사람 수 구하기
    for i in times :
        total += mid // i
        
    if total >= m :
        res = mid
        end = mid - 1
        
    else :
        start = mid + 1
        
print(res)
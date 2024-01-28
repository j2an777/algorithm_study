#1. 질투심이 가장 낮게 나오기 위해서는 모두한테 줘야하고, 최대한 골고루 줘야함

import math

n, m = map(int, input().split())
color = []
for i in range(m) :
    color.append(int(input()))

# 모든 어린이가 1개씩 받을 때
start = 1

# 한 명이 한 색상 모두 가질 때
end = max(color)

res = 0

while start <= end :
    mid = (start + end) // 2
    
    total = 0
    
    # 색상 개수에서 mid에 나눠 떨어지면 그 몫이 나누는 아이들 수, 나눠 떨어지지 않으면 몫+1 명
    for i in color :
        total += math.ceil(i / mid)
    
    # 나눠지게 되는 어린이 수가 해당 수보다 작거나 같으면 나누는 개수를 줄이기
    if total <= n :
        res = mid
        end = mid - 1
    
    # 오히려 나눠지게 되는 어린이 수가 더 크다면 나누는 개수 늘리기
    else :
        start = mid + 1
    
    
print(res)
#1. total이 i 보다 작다면 cnt 1 증가 및 total에 mid 더해주기(1회 충전)
#2. 충전했는데도 값이 부족하다면 


n, m = map(int, input().split())
pay = []

for i in range(n) :
    pay.append(int(input()))

# 아예 값이 적어서 인출 못하는 상황을 배제
start = max(pay)
end = sum(pay)

res = 0

while start <= end :
    mid = (start + end) // 2
    
    cnt = 1
    total = mid
    
    for i in pay :
        # 해당값이 충전한 값보다 크면 카운트 해주고, 다시 mid값 충전
        if i > total :
            cnt += 1
            total = mid
        
        # 충전한 값에서 해당 값 빼주기
        total -= i
    
    # 카운트 수가 m 보다 크다면 mid값 올려주기
    if cnt > m :
        start = mid + 1
    
    # 카운트 수가 m 보다 작거나 같다면 값 내려주기
    else :
        res = mid
        end = mid - 1
        
print(res)
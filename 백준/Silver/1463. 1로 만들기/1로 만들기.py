n = int(input())
dp = [0] * (n + 1)

if n >= 2 :
    dp[2] = 1
if n >= 3 :
    dp[3] = 1

for i in range(4, n+1) :
    # 현 인덱스 값의 최소 연산 횟수
    dp[i] = dp[i-1] + 1
    
    # 2의 배수 일 때, 몫을 가지는 인덱스의 값 +1
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    # 3의 배수 일 때, 몫을 가지는 인덱스의 값 +1
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i // 3] + 1)
    
print(dp[n])
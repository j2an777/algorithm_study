h, y = map(int, input().split())
dp = [0] * (y + 1)
dp[0] = h

for i in range(1, y + 1) :
    dp[i] = dp[i - 1] + dp[i - 1] * 5 // 100
    
    if i >= 3 :
        dp[i] = max(dp[i], dp[i - 3] + dp[i - 3] * 20 // 100)
        
    if i >= 5 :
        dp[i] = max(dp[i], dp[i - 5] + dp[i - 5] * 35 // 100)

print(dp[y])
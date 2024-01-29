n = int(input())
dp = [0] * (n + 1)

# 1회 돌렸을 때 시점
dp[0] = 0
dp[1] = 1

if n == 1 :
    print(dp[0], dp[1])

else :
    for i in range(2, n+1) :
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[n-1], dp[n])
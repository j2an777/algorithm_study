n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]
mod = 10007

for i in range(10) :
    dp[0][i] = 1

for i in range(1, n) :
    for j in range(10) :
        for k in range(0, j+1) :
            dp[i][j] += dp[i-1][k]
            
res = sum(dp[-1]) % mod
print(res)
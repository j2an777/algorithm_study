n = int(input())
dp = [1] * 10
res = 0
mod = 10007

for i in range(n-1) :
    for j in range(1, 10) :
        dp[j] += dp[j-1]
        
res = sum(dp) % mod
print(res)

n = int(input())
dp = []

for i in range(n) :
    dp.append(list(map(int, input().split())))
    
for i in range(0, n-1) :
    dp[i+1][0] += min(dp[i][1], dp[i][2])
    dp[i+1][1] += min(dp[i][0], dp[i][2])
    dp[i+1][2] += min(dp[i][0], dp[i][1])
    
print(min(dp[n-1]))
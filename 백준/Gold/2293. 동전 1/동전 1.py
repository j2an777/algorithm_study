n, k = map(int, input().split())
num = []
for i in range(n) :
    num.append(int(input()))
    
dp = [0] * (k + 1)
dp[0] = 1

for i in num :
    for j in range(1, k + 1) :
        if j >= i :
            dp[j] += dp[j - i]
            
print(dp[k])
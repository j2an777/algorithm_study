t = int(input())
res = []

for i in range(t) :
    res.append(int(input()))
    
for i in res :
    dp = [0] * (i + 1)
    
    for j in range(1, i + 1) :
        if j == 1 :
            dp[1] = 1
        elif j == 2 :
            dp[2] = 2
        elif j == 3 :
            dp[3] = 4
        else :
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
            
    print(dp[-1])
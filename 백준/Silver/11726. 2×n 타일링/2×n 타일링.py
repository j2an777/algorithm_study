n = int(input())
dp = [0] * (n)

mod = 10007

if n == 1 :
    print(1 % mod)
    
elif n == 2 :
    print(2 % mod)
    
else :
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n) :
        dp[i] = (dp[i-1] + dp[i-2]) % mod
    
    print(dp[n-1])
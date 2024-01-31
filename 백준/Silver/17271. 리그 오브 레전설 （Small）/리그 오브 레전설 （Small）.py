#1. 주어진 M에 대해서 1초와 M초로 N초 까지의 모든 경우의 수를 고려

n, m = map(int, input().split())
dp = [0] * (n + 1)
mod = 1000000007
    
for i in range(0, n + 1) :
        
    # i가 m초 보다 적을 때까지는 경우의 수는 1개
    if i < m :
        dp[i] = 1

    else :
        dp[i] = (dp[i-1] + dp[i-m]) % mod
    
        
print(dp[n])
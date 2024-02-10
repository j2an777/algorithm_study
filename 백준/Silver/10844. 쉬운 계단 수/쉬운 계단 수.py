n = int(input())

mod = 1000000000

#첫 번째 숫자 0~10 (1부터 시작이기 때문) 세트를 n 만큼 생성
dp = [[0] * 10 for _ in range(n + 1)]

# n = 1일 때는 모두 1 대입
for i in range(1, 10) :
    dp[1][i] = 1
    
for i in range(2, n + 1) :
    for j in range(10) :
        if j == 0 :
            dp[i][j] = dp[i-1][1]
        elif j == 9 :
            dp[i][j] = dp[i-1][8]
        else :
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % mod)
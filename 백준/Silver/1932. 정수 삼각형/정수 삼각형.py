n = int(input())
num = []

for i in range(n) :
    num.append(list(map(int, input().split())))
    
dp = [[0] * (i + 1) for i in range(n)]

dp[0][0] = num[0][0]

for i in range(1, n) :
    for j in range(i+1) :
        # 각 열의 0번째 행은 그 위의 열의 0번째 행과 합
        if j == 0 :
            dp[i][j] = dp[i-1][j] + num[i][j]
        # 각 열의 마지막 행은 그 위의 열의 마지막 행
        elif j == i :
            dp[i][j] = dp[i-1][j-1] + num[i][j]
        # 그 외 나머지 행들은 왼쪽 위와 바로 위 중 최댓값으로 합
        else :
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + num[i][j]
        
print(max(dp[-1]))
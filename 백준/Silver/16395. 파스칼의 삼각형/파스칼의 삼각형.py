n, k = map(int, input().split())
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(0, n) :
    for j in range(0, i + 1) :
        
        # 0번째 열, 1열 이후 부터는 0행과 마지막행에 1
        if i == 0 or j == 0 or j == i :
            dp[i][j] = 1
        
        # 나멎;는 각 인덱스에 n-1열에 n-1행과 n행의 합을 넣기  
        else :
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            
print(dp[n-1][k-1])
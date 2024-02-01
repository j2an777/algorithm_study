# lis 알고리즘
# 비교하려는 인덱스를 기준으로 0부터 기준까지 값을 비교해서 크다면 dp 값 갱신

a = int(input())
listA = list(map(int, input().split()))
dp = [0] * a

for i in range(0, a) :
    # 해당 회차에서 1로 시작
    dp[i] = 1
    for j in range(0, i) :
        # 0부터 해당 인덱스까지의 값들 비교해서 비교하고자 하는 값이 더 크다면
        if listA[j] < listA[i] :
            # 해당 j인덱스 dp 값 +1한 값과 비교해서 최댓값 갱신
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))
def dfs(x, y):
    # 탐색이 삼각형의 범위를 벗어났는지 확인
    if x >= n:
        return 0
    # 이미 방문한 노드의 최대 합이 계산되어 있다면 재활용
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 현재 위치에서 선택할 수 있는 두 경로 중 최대 합을 찾아 현재 노드 값과 합산
    dp[x][y] = triangle[x][y] + max(dfs(x + 1, y), dfs(x + 1, y + 1))
    return dp[x][y]

n = int(input())
triangle = []
dp = [[-1 for _ in range(n)] for _ in range(n)]  # 메모이제이션을 위한 DP 테이블 초기화

for i in range(n):
    triangle.append(list(map(int, input().split())))

print(dfs(0, 0))

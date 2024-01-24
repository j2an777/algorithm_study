x, y = map(int, input().split())

# 승률
z = (y * 100) // x

# 승률이 99퍼 이상이라면
if  z >= 99 :
    print(-1)

else :
    # 최소 한 판은 시행
    start = 1
    
    # 범위를 최대 (지금까지 게임 횟수로 지정)
    end = x
    
    # 최소 횟수 결과
    res = 0

    while start <= end :
        # start, end 사이의 중간 횟수
        mid = (start + end) // 2
        
        # 추가 횟수 더한 승률이 기존 승률보다 높다면
        if ((y + mid) * 100) // (x + mid) > z :
            # 추가 횟수를 res에 갱신
            res = mid
            end = mid - 1
        
        else :
            start = mid + 1
        
    print(res)
a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))
b.sort()

def findtarget(i) :
    start = 0
    end = a - 1
    
    while start <= end :
        mid = (start + end) // 2  #이분탐색 위한 중앙인덱스
        
        if b[mid] == i :
            return True
        elif i < b[mid] :
            end = mid - 1
        else :
            start = mid + 1

for i in range(len(d)) :
    if (findtarget(d[i])) :
        print(1)
    else :
        print(0)
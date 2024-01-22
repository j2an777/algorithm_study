def binary_search(array, target, start, end) :
    
    while start <= end :
        mid = (start + end) // 2
        
        if array[mid] == target :
            return True
        
        elif array[mid] < target :
            start = mid + 1
            
        else :
            end = mid - 1
            
    return False

n = int(input())
nBox = list(map(int, input().split()))
    
m = int(input())
mBox = list(map(int, input().split()))

nBox.sort()

for num in mBox :
    if binary_search(nBox, num, 0, n-1) :
        print(1)
    else :
        print(0)
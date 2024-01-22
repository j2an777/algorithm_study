def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        
        if array[mid] == target :
            return True
        
        elif array[mid] > target :
            end = mid - 1
        
        else :
            start = mid + 1
    
    return False

a, b = map(int, input().split())
aBox = list(map(int, input().split()))
bBox = list(map(int, input(). split()))

aBox.sort()
newBox = set()
res = []

for i in bBox :
    if binary_search(aBox, i, 0, a-1) :
        newBox.add(i)

for i in aBox :
    if i not in newBox :
        res.append(i)

if len(res) == 0 :
    print(0)
else :
    print(len(res))
    for i in res :
        print(i, end=" ")
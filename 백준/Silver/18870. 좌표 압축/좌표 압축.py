from bisect import bisect_left, bisect_right


n = int(input())
nBox = list(map(int, input().split()))

newSet = set(nBox)
newList = list(newSet)
newList.sort()

for i in nBox :
    boxIndex = bisect_left(newList, i)
    print(boxIndex, end=" ")
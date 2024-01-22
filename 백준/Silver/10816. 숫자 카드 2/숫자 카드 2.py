from bisect import bisect_left, bisect_right

n = int(input())
nBox = list(map(int, input().split()))

nBox.sort()

m = int(input())
mBox = list(map(int, input().split()))

for i in mBox :
    left_index = bisect_left(nBox, i)
    right_index = bisect_right(nBox, i)
    res = right_index - left_index
    print(res, end = " ")
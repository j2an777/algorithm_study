n = int(input())
amount = [int(input()) for i in range(0, n)]
res = []

amount.sort()
cnt = len(amount)

for i in range(0, n) :
    res.append(amount[i]*cnt)
    cnt -= 1

print(max(res))
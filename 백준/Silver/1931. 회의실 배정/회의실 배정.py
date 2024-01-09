n = int(input())
k = []
cnt = 1

for i in range(n) :
    k.append(list(map(int, input().split())))

k.sort(key=lambda x: (x[1], x[0]))
et = k[0][1]

for i in range(1, n) :
    if k[i][0] >= et :
        cnt += 1
        et = k[i][1]

print(cnt)
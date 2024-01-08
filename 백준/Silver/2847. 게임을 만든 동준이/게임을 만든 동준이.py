n = int(input())
k = []
cnt = 0

for i in range(0, n) :
    k.append(int(input()))

for i in range(n-1, 0, -1) :
    if k[i-1] - k[i] >= 0 :
        cnt += k[i-1] - k[i] + 1
        k[i-1] = k[i] - 1
    else :
        continue
    
print(cnt)
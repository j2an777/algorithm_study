a = int(input())
cnt = 0
s = 1

for i in range (1, a+1) :
    s = s * i

nList = list(map(int, str(s)))

for i in range(len(nList), 0, -1) :
    if (nList[i-1] == 0) :
        cnt = cnt + 1
    else : 
        break

print(cnt)
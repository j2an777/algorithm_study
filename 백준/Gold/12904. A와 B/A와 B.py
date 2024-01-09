n = list(input())
res = list(input())

for i in range(len(res)-1, len(n)-1, -1) :
    if res[i] == 'A' :
        res.pop()
    elif res[i] == 'B' :
        res.pop()
        res.reverse()

if n == res :
    print(1)
else :
    print(0)
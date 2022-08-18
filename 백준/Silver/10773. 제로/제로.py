a = int(input())
c = []

for i in range(a) :
    b = int(input())
    if (b == 0) :
        del c[-1]
    else :
        c.append(b)

sum = 0
for i in c :
    sum = sum + i
print(sum)
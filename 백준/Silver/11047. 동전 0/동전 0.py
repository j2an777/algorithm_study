inn = list(map(int, input().split()))
res = 0
sel = []

for i in range(0, inn[0]) :
    num = int(input())
    sel.append(num)
    
sel.sort(reverse=True)
total = inn[1]

for coin in sel :
    if total >= coin :
        res += total // coin
        total %= coin
        
print(res)
n = int(input())
ctlen = list(map(int, input().split()))
price = list(map(int, input().split()))
minprice = price[0]
res = 0

# 2번 내용 반영으로 n-1로 진행
for i in range(n-1) :
    if price[i] <= minprice :
        minprice = price[i]
    res += ctlen[i] * minprice
    
print(res)
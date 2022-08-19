n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

list_a = sorted(a, reverse = True)
list_b = sorted(b)

list_sum = 0
for i in range(n) :
    list_sum += list_a[i] * list_b[i]
    
print(list_sum)
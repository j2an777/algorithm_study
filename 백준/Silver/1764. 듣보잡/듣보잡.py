import sys

n, m = map(int, input().split())

dic = {}
for i in range(n+m):  
    name = sys.stdin.readline().strip()
    
    if name not in dic:  
        dic[name] = 1
    
    else:
        dic[name] = dic[name]+1  

answer = []
for k, v in dic.items():  
    if v == 2:
        answer.append(k)
print(len(answer))
print("\n".join(sorted(answer)))  
t = int(input())
for i in range(t) :
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    s1 = [0 for i in range(n)]
    s1[m] = 1
    cnt = 0
    
    while True :
        if s[0] == max(s) :
            cnt += 1
            if s1[0] == 1 :
                print(cnt)
                break
            else :
                del s[0]
                del s1[0]
        else :
            s.append(s[0])
            del s[0]
            s1.append(s1[0])
            del s1[0]
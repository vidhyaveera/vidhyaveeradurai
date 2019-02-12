m=int(input())
m1=list(map(int,input().split()))
m2=list(map(int,input().split()))
for i in range(m):
    for j in range(m):
        if m1[i]==m2[j]:
            print(m1[i])
            break

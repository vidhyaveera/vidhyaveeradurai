n=int(input())
m=list(map(int,input().split()))
#l=list(str(m))
for i in range(n):
    if m.count(i)==1:
        print(i)
        

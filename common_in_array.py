n=int(input())
m=list(map(int,input().split()))
m1=list(map(int,input().split()))
for i in m:
    if i in m1:
        print(i,end=" ")

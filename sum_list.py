m,n=map(int,input().split())
m1=list(map(int,input().split()))
for i in range(m):
    for j in range(i+1,m):
        if m1[i]+m1[j]==n:
            print("yes")
            exit(0)
        
else:
    print("no")

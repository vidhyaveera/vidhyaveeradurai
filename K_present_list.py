m,l=map(int,input().split())
n=list(map(int,input().split()))
for i in range(m):
    if l==n[i]:
        print("yes")
        break
else:
    print("no")
    

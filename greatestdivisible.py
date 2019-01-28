m,n=map(int,input().split())
a=m*n
b=[]
for i in range(a,0,-1):
    if m%i==0 and n%i==0:
        b.append(i)
print(max(b))

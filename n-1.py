m,n=map(int,input().split())
m1=list(map(int,input().split()))
a=[]
for i in range(len(m1)):
    if m1[i]<n:
        a.append(m1[i])
a.sort()
for i in range(len(a)):
    if i==len(a)-1:
        print(a[i],end="")
    else:
        print(a[i],end=" ")
       #vidhya

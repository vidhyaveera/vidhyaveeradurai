n,m,l=map(str,input().split())
l=int(l)
c=0
if(len(n)!=len(m)):
    print("no")
else:
    for i in range(len(n)):
        if n[i]!=m[i]:
            c+=1
if c==l:
    print("yes")
else:
    print("no")

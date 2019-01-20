a,b=list(map(int,input("").split()))
c,d=list(map(int,input("").split()))
if(a>c and b<d):
    a=a-1
    b=b+60
    print(a-c,b-d)
elif a<c and b>d:
    s=c-a
    w=b-d
    print(s,w)
elif a<c and b<d:
    print(c-a,d-b)
else:
    print(a-c,b-d)

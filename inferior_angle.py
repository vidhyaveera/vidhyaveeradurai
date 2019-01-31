n,m,a=map(int,input().split())
if n>0 and m>0 and a>0:
    b=n+m+a
    if b==180:
        print("yes")
else:
    print("no")

n=int(input(""))
m=1
v=1
c=0
print(m,v,end=" ")
for i in range(2,n):
    c=m+v
    print(c,end=" ")
    m=v
    v=c

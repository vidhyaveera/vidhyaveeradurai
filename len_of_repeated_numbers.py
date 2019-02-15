a=int(input())
t=list(map(int,input().split()))
c=0
max=0
for j in t:
    for i in t:
        if i==j:
            c+=1
        if c>max:
            max=c
    c=0
print(max)

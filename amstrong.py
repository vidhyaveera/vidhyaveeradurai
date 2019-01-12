num=int(input(""))
c=num
sum=0
while num>0:
    r=num%10
    sum=sum+r*r*r
    num=num//10
if sum==c:
    print("yes")
else:
    print("no")

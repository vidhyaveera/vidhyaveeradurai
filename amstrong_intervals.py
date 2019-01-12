a,b=map(int,input("").split())
def printamstrong(c):
    num=c
    sum=0
    while num>0:
        r=num%10
        sum=sum+r*r*r
        num=num//10
    if sum==c:
        return True
    else:
        return False
for i in range(a,b+1):
     if(printamstrong(i)):
         print(i,end="")
    

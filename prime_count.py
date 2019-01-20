a,b=map(int,input("").split())
def isprime(c):
    for i in range(2,c):
        if(c%i==0):
            return False
    else:
        return True
c=0
for i in range(a,b+1):
    if(isprime(i)):
        c+=1
print(c)

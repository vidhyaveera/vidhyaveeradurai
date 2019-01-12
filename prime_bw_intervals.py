a,b=map(int,input("").split())
def isprime(c):
    for i in range(2,c):
        if(c%i==0):
            return False
    else:
        return True
        
for i in range(a+1,b):
    if(isprime(i)):
        print(i,end=" ")

a,b=map(int,input("").split())
for i in range(a+1,b):
    if(i%2==0):
        if(i==a+1 or i==a+2):
            print(i,end="")
        else:
            print(" ",i,end="")
        

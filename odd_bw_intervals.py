a,b=map(int,input("").split())
for i in range(a+1,b):
    while(i%2!=0):
        print(i,end=" ")
        break
        i=i+1

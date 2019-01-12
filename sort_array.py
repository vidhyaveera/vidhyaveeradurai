a=int(input(""))
b=list(map(int,input("").split()))
for i in range(len(b)):
    for j in range(len(b)):
        if(b[i]<b[j]):
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
for i in range(len(b)):
    print(b[i],end=" ")
           

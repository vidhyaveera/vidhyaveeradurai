N,K=map(int,input("").split())
lst=list(map(int,input().split()))
c=0
for i in range(K):
    temp=lst[-1]
    del(lst[-1])
    lst.insert(0,temp)
    
for i in range(len(lst)):
    if(c==0):
         print(lst[i],end="")
         c+=1
    else:
        print("",lst[i],end="")

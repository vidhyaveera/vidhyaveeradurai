s,n=map(str,input().split())
c=0 #declare count =0
for i in range(0,len(s)):
    for j in range(0,len(n)):
        if  i==j:
            #check the index
            if s[i]!=n[i]:
                c+=1
if c==1:
    print("yes")
else:
    print("no")

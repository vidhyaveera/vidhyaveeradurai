m=int(input(""))
i=0
n=2
while n<=m:
    a=2**i
    if a==m:
        print("yes")
        break
    i+=1
else:
    print("no")

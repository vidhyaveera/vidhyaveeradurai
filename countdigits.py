a=int(input(""))
count=0
if a==0:
    count=1
while a>0:
    count=count+1
    a=a//10
print(count)    
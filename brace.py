n=input()
a=b=0
for i in n:
    if i==")":
        a+=1
    elif i=="(":
        b+=1
if a==b:
    print("yes")
else:
    print("no")

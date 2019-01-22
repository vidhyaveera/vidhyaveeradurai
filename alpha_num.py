n=input("")
c=0
d=0
for i in range(len(n)):
    if n[i].isalpha():
        c+=1
    elif n[i].isdigit():
       d+=1
if c>0 and d>0:
    print("yes")
else:
    print("no")


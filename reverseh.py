n=input()
n1=n.split()
d=[]
for i in n1:
    d.append(i[::-1])
print(*d)
 

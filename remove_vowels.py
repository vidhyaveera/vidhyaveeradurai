m=int(input())
n=input()
s=n[::-1]
l=list(str(s))
for i in l:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        l.remove(i)
        b= ''.join(map(str, l))
print(b)

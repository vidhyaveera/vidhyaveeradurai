n=input()
l=list(n)
for i in range(0,len(n)):
    if n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o'or n[i]=='u':
        print("yes")
        break
    
else:
    print("no")

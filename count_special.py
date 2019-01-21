n=input("")
c=['@','!','#','$','%','^','&','*','.','?']
count=0
for i in n:
    if i in c:
        count+=1
print(count)        

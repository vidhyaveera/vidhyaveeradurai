a,b=map(int,input().split())
t=list(map(int,input().split()))
for j in t:
    if j==b:
      print("yes")
      break
else:
    print("no")

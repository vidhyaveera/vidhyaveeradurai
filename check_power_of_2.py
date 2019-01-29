n=int(input())
for i in range(n):
    if n==2**i:
        print("yes")
        break
else:
    print("no")

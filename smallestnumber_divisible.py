l,r=map(int,input().split())
a=l*r
for i in range(1,a+1):
      if i%l==0 and i%r==0:
            print(i)
            break
            #vidhya

a=input()
n=[x for x in a]
s=""
for i in range(0,len(a),2):
    n[i],n[i+1]=n[i+1],n[i]
    s=s+n[i]+n[i+1]
print(s)

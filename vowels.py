a1=['A','E','I','O','U']
c=input("")
b=c.upper()
if ord(b)>=65 and ord(b)<=90:
    for i in range(len(a1)):
        if(a1[i]==b):
            print("vowels")
            break
    else:
        print("consonants")
else:
    print("invalid")


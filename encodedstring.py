value = input()
value=value.upper()
a=''.join(map(lambda x:chr(ord(x)+3),value))
print(a)

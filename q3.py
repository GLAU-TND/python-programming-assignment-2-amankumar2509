x=int(input())
a=bin(x)
print(a)
a=a[2:]
print (max(map(len, a.split('0')))) 

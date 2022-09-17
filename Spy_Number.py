n=int(input())
s=0
p=1
for i in str(n):
    i=int(i)
    s+=i
    p*=i
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
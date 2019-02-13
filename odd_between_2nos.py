n1,n2=map(int,input().split())
c=""
for a in range(n1+1,n2):
    if a%2==1:
        c=c+str(a)+" "
print(c.strip())

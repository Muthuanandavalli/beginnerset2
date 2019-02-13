n1,n2=map(int,input().split())
a=""
for b in range(n1+1,n2):
    if b%2==0:
        a=a+str(b)+" "
print(a.strip())
       

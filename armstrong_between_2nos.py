a1,a2=map(int,input().split())
for i in range(a1+1,a2):
    n=i
    s=0
    while n>0:
        r=n%10
        s=s+(r*r*r)
        n=n//10
    if s==i:
        print(i)
    

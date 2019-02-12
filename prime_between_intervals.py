N,K=map(int,input().split())
flag=0
for i in range(N+1,K):
 for j in range(2,i):
  if i%j==0:
   flag=1
   break
 else:
     print(i,end=" ")

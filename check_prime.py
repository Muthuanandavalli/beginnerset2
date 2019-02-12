N=int(input())
flag=0
if N<=1000:
 for i in range(2,N-1):
  if N%i==0:
   flag=1
   break
if flag==1:
 print("no")
else:
 print("yes")

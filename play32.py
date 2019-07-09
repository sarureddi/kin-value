n,k=map(int,input().split())
lis=list(map(int,input().split()))
lent=len(lis)
count=0
for i in range(0,lent):
  if(k==lis[i]):
    count=count+1
  else:
    continue
if(count==0):
  print("no")
else:
  print("yes")

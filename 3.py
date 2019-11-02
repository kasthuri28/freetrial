n=int(input())
for i in range (n+1) :
  for j in range (n-1) :
    print("  ",end=" ")
  for k in range(i) :
    print (2**k,end=" ") 
  for p in range(i,-1,-1) :
    print (2**p,end=" ")
  print()

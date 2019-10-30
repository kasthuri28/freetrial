k=int(input())
a=[]
for i in range (k) :
  x=int(input())
  a.append(x)
n=int(input("enter the search key"))
b=0
e=len(a)-1
while (b<=e):
 m=(b+e)//2
 if(a[m]==n) :
    print ('found in position',m+1)
    break
 elif(a[m]>n):
    e=m-1
 else :
    b=m+1


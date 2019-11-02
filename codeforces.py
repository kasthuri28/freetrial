a=input()
b="bcdfghjklmpqrstvwxyz"
c="aeiou"
l=1
for i in a :
 if i in b :
   f=a.index(i)
   if a[f+1] not in c :
     print ("NO")
     l=0
     break
if (l==1) :
 if (a[len(a)-1]=="n") :
    print("YES")
 elif a[len(a)-1] in c :
    print("YES")
 else : 
    print("NO")

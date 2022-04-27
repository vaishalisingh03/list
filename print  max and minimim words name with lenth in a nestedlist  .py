a=["meena","vaishali","teena","omio","week"]
i=0
l=[]
b=[]
while i<len(a[i]):
        if len(a[i])%2==0:
            l.append([a[i],len(a[i])])
        else:
            b.append([a[i],len(a[i])])
        i+=1 
print(l,b)        

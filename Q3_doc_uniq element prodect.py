a=[6,1,3,5,6,3,1]
i=0
l=[]
while i<len(a):
    if a[i] not in l:
        l.append(a[i])
        j=0
        prod=1
        while j<len(l):
            prod*=a[j]
            j+=1
    i+=1
print(prod)
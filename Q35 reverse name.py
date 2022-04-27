a=["divya","kiran","nilu"]
l=len(a)
i=0
b=[]
while i<l:
    j=1
    sum=""
    while j<len(a[i])+1:
        sum+=a[i][-j]
        j+=1
    b.append(sum)
    i+=1
print(b)


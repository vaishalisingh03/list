a=["a","n","t","a","a","e","a","t","n","t"]
i=0
l=[]
m=[]
while i<len(a):
    if a[i] not in l:
        l.append(a[i])
        j=0
        count=0
        while j<len(a):
            if a[i]==a[j]:
                count+=1
            j+=1
        print(count,a[i])
    i+=1

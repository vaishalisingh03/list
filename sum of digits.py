list=[12,23,45,123]
i=0
while i<len(list):
    a=str(list[i])
    j=0
    sum=0
    while j<len(a):
        sum+=int(a[j])
        j+=1
    i+=1
    print(sum)
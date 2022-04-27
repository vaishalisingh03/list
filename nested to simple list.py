a=[1,[2],[2,3],[3],4]
i=0
l=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            l.append(a[i][j])
            j+=1
    else:
        l.append(a[i])
    i+=1
print(l)
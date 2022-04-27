n=[10,11,12,13,14,17,18,19]
number=30
list=[]
i=0
while i<len(n):
    j=0
    while j<len(n):
        a=n[i]
        m=n[j]
        if n[i]+n[j]==number:
            list.append([a,m])
        j+=1
    i+=1
print(list)

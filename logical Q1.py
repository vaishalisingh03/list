list=[8,-2,7,-1,-3,9,4]
i=0
a=[]
while i<len(list):
    if list[i]<0:
        a.append(0)
    else:
        a.append(list[i])
    i+=1
print(a)
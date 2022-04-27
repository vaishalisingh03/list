list=[9,4,3,1,7,8,2,6]
i=0
while i<len(list):
    j=i+1
    while j<len(list):
        if list[i]>list[j]:
            c=list[i]
            list[i]=list[j]
            list[j]=c
        j+=1
    i+=1
print(list)




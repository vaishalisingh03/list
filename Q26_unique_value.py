list=[1,2,2,5,8,4,4,8]
a=[]
i=0
count=0
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
        count+=1
    i+=1
print(a,"are uniquef unique value",count)





list=[1,2,3]
i=0
count=0
list1=[]
while i<len(list):
    list1.append(list[i])
    if count==1:
        list1.append(10)
    count+=1
    i+=1
print(list1)

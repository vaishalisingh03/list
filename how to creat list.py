num=int(input("enter number of element"))
list=[]
i=0
while i<num:
    num1=int(input("enter element"))
    list.append(num1)
    i=i+1
j=0
list1=[]
while j<len(list):
    if list[j] not in list1:
        list1.append(list[j])
    j+=1
print(list1)
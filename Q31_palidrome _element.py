list1=["mom","sai","made","sis"]
i=0
a=[]
b=[]
count=0
while i<len(list1):
    str=list1[i]
    j=1
    sum=""
    count=0
    while j<len(list1[i])+1:
        sum+=list1[i][-j]
        j+=1
    if str==sum:
        a.append(sum)
    else:
        b.append(sum)
    i+=1
print("this elemsnts is palimdrom",a)
print("this elements is not palimdrom",b)


a=[1,2,3,[4,5,6],7,8]
l=len(a)
i=0
count=0
count1=0
while i<l:
    if type(a[i])==list:
     j=0
     while j<len(a[i]):
        count+=1
        j+=1
    else:
        count+=1
    i+=1
print(count)











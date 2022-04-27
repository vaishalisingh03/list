a=[[1,2,3,4,7,9],[3,7,6],[2,8,9,5,3,6,2,7]]
i=0
count1=0
count2=0
count3=0
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        if i==0:
            count1+=1
        elif i==1:
            count2+=1
        else:
            count3+=1
        j+=1
    i+=1
print(count1)
print(count2)
print(count3)
money=[3000,5600000,324990909,90990900,532010,31010101,510,30000,600000,123]
i=0
count=0
count1=0
count2=0
while i<len(money):
    if  money[i]>=10000000:
        count+=1
    elif money[i]>=100000:
        count1+=1
    elif money[i]<100000:
        count2+=1
    i=i+1
print("carorpati",count)
print("lakhpati",count1)
print("dilwale",count2)


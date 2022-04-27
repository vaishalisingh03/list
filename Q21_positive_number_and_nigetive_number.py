list=[1,-2,3,-4,5,-6,7,-8,9,-10,11]
i=0
count=0
count1=0
positiv=[]
nigetive=[]
while i<len(list):
    if list[i]>0:
        positiv.append(list[i])
        count+=1
    elif list[i]<0:
        count1+=1
        nigetive.append(list[i])
    i+=1
print("positiv number in list",positiv)
print("nigetive number in list",nigetive)
print("how many positiv number in list",count)
print(" how many nigetive number in list",count1)

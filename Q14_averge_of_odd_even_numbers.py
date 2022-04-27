list=[23,14,56,12,19,9,15,25,31,42,43]       
sum=0
sum1=0
count=0
count1=0
i=0
while i<len(list):
    if list[i]%2!=0:
        sum+=list[i]
        count+=1
    elif list[i]%2==0:
        sum1+=list[i]
        count1+=1    
    i+=1
print("averg of odd numbers",sum/count)
print("averg of even numbers",sum1/count1)


list=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
sum1=0
count=0
count1=0
while i<len(list):
    if list[i]%2!=0:
        sum+=list[i]
        count+=1
    elif list[i]%2==0:
        sum1+=list[i]
        count1+=1
    i+=1
print("count of odd numbers=",count)
print("count of even numbers=",count1)
print("count of all numbers=",count+count1)
print("sum of odd numbers=",sum)
print("sum of even numbers=",sum1)
print("sum all of numbers=",sum+sum1)
print("averg of odd numbers=",sum/count)
print("averg of even numbers=",sum1/count1)
print("averg of all numbers=",sum+sum1/count+count1)

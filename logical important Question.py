a=[1,2,3,4,5]
num=int(input("enter number:>"))
i=0
sum=0
while i<len(a):
    if a[i]>num:
        sum+=a[i]
    i+=1
print(sum)
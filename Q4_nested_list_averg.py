a=[[3,8,9,6,4,5],[7,8,9],[3,7,8,9,6,5,3,2]]
l=len(a)
i=0
sum=0
count=0
while i<l:
    j=0
    while j<len(a[i]):
        sum+=a[i][j]
        count+=1
        j+=1
    i+=1
print("sum=",sum,"count=",count,"averg=",sum/count)






        


            
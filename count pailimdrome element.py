a=["oyo","mom","dad","nitin","sai"]
i=0
count=0
lenth=len(a)
b=[]
while i<lenth:
    lenth-=1
    b.append(a[i])
    if b==a:
        print(b)
    else:
        i+=1
    count+=1
print(count,"palimdrome :",b)


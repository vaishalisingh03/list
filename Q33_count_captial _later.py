n=input("enter the word")
a=list(str(n))
sum=""
i=0
while i<len(a):
    sum=sum+a[i]
    i+=1
p=sum.split()
count=0
count1=0
j=0
while j<len(p):
    l=0
    while (l<len(p[j])):
        if (p[j][l]==p[j][l].upper()):
            count+=1
        else:
            count1+=1
        l+=1
    j+=1
print("capital latter is",count)
print("small latter is",count1)


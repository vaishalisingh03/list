list=[6,8,3,4,11,9]
i=0
while i<len(list):
    a=list[i]
    j=1
    count=0
    while j<len(list):
        if list[i]%j==0:
            count+=1
        j+=1
    i+=1
    if count==2:
        print(a,"prime number")
    else:
        print(a,"not prime number")
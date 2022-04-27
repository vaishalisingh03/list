list=[6,4,12,28,7,8]
i=0
while i<len(list):
    a=list[i]
    org=list[i]
    j=1
    sum=0
    while j<a:
        if list[i]%j==0:
            sum+=j
        j+=1
    i+=1
    if org==sum:
        print(a,"perfect number")
    else:
        print(a,"not perfect number")

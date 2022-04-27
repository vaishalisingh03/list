list=[153,123,370,521,371]
i=0
while i<len(list):
    sum=0
    org=list[i]
    while list[i]>0:
        sum=sum+(list[i]%10)**3
        list[i]//=10
    i+=1
    if org==sum:
        print("armstrong number is",sum)
    else:
        print("not armstrong number",sum)


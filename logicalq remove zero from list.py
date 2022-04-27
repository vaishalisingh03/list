a=[10,1203,10101,123031]
i=0
b=[] 
while i<len(a):
    s=str(a[i])
    sum=""
    j=0
    while j<len(s):
        if s[j]=="0":
            pass
        else:
            sum+=s[j]
        j+=1
    b.append(int(sum))
    i+=1
print(b)
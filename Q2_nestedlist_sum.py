list=[["v","a","i"],["s","h","a"],["l","i"]]
i=0
sum=""
while i<len(list):
    j=0
    while j<len(list[i]):
        sum+=list[i][j]
        j+=1
    i+=1
print(sum)      

                        
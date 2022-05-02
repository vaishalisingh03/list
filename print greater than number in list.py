a=[1,2,3,4,5,6,7,8,9,10]
num=int(input("enter number"))
i=0
while i<len(a):
    if a[i]<num:
        print(a[i])
        break
    i+=1

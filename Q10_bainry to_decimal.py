list=[1,0,0,1,1,0,1]
l=len(list)
sum=0
a=0
i=l-1
while i>-1:
      sum=sum+list[i]*(2**a)
      i=i-1
      a=a+1
print("bainry to decimal number is",sum)









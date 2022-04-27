list=[50,40,23,72,70,56,12,5,7]
max=0
second_max=0
third_max=0
i=0
while i<len(list):
    j=0
    while j<len(list):
      if list[j]>max:
        max=list[j]
      if list[j]>second_max and list[j]!=max:
        second_max=list[j]
      if list[j]>third_max and list[j]!=second_max and list[j]!=max:
        third_max=list[j]
      j+=1
    i=i+1
print("maximam number",max)
print("second maximam number",second_max)
print("third maximam number",third_max)
    
    

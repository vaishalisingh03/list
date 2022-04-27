magic_square=[[8,3,4],
[1,5,9],
[6,7,2]]
row_sum=0
i=0
while i<len(magic_square):
    j=0
    while j<len(magic_square):
        row_sum+=magic_square[i][j]
        j+=1
    i+=1
    print(row_sum)
    print()
i=0
col_sum=0
while i<len(magic_square):
    j=0
    while j<len(magic_square):
        col_sum+=magic_square[i][j]
        j+=1
    i+=1
    print(col_sum)
    print()
i=0
left_diagonal=0
while i<len(magic_square):
    left_diagonal+=magic_square[i][i]
    i+=1
    print(left_diagonal)
j=2
i=0
right_diagonal=0
while i<len(magic_square):
    right_diagonal+=magic_square[i][j]
    i+=1
    j-=1
print(right_diagonal)
print()
print(row_sum,col_sum,left_diagonal,right_diagonal)
if row_sum==col_sum and left_diagonal==right_diagonal:
    print("it is a magic square",row_sum,col_sum,left_diagonal,right_diagonal)
else:
    print("it is not magic sqare",row_sum,col_sum,left_diagonal,right_diagonal)
    

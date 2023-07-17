def rotate_matrix(r,c,matrix):
    temp=0
    for i in range(r):
        for j in range(r):
            if i<j:
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
    matrix = [row[::-1] for row in matrix]
    return matrix

matrix=[]
r=int(input("Number of Rows : "))
c=int(input("Number of Columns : "))
for i in range(r):
    matrix.append(list(map(int,input().split())))
print(rotate_matrix(r,c,matrix))
def matmul(a,b):
    c=[]
    for i in range(len(a)):
        c.append([])
        for j in range(len(b[0])):
            sum=0
            for k in range(len(b)):
                sum=sum+a[i][k]*b[k][j]
            c[i].append(sum)
    print("the answer is",c)
def getmatrix(r,c):
    mat=[]
    for ro in range(r):
        mat.append([])
        for co in range(c):
            mat[ro].append(int(input("enter the element [{}][{}]".format(ro,co))))
    return mat        
    
    
r1=int(input("enter the no rows in matrix a"))
c1=int(input("enter the no columns in matrix a"))
r2=int(input("enter the no rows in matrix b"))
c2=int(input("enter the no columns in matrix b"))
if c1==r2:
    a=getmatrix(r1,c1)
    b=getmatrix(r2,c2)
    matmul(a,b)
else:
    print("matrix multiplication is not possible")




                
            
        

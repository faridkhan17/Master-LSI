n = 3
m = 3
#wrong
row = [0]*n
mat=[]
for i in range(m):
    mat.append(row)
    mat[0][1]=3
print(mat)    
#right
mat = []
for i in range(m):
    row = [0]*n
    mat.append(row)
    mat[0][1]=3
print(mat)


'''output
[[0, 2, 0], [0, 2, 0], [0, 2, 0]]
[[0, 2, 0], [0, 0, 0], [0, 0, 0]]
'''
#with this code , one element cannot be changed, as in example mat[0][2] = 2, it 
#changes middle element in all the lists. which is not desired. it is because it is saved by reference
    

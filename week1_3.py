################

# Author: Zane Dawson

# Date: 09/11/2019

# This program takes a predeterminded matrix

# and then transposes it. The program then multiplies

# the two matricies together.

################ 


#variable initialization
matrix = [[2, -5, 8, 11], [3, 7, -9, -5], [4, 0, -1, 7]] #given matrix
rows = len(matrix) #number of rows in matrix
colms = len(matrix[0]) #number of columbs in matrix
tranMat = [] #transmuted matrix
matFin = [] #array of matrix after multiplication
multMat = [] #finished multiplied matrix
matSum = 0 #sum of matrix multiplication
k = 0 #counter variable
v = 0 #counter variable
m = 0 #counter variable
i = 0 #counter variable

#loops through the columbs
for i in range(colms):
    tranMatRow = [] #transmuted row of matrix
    for j in range(rows): #loops through the rows of the matrixes
        #appends the matrix value from the original matrix to new row
        tranMatRow.append(matrix[j][i])
    tranMat.append(tranMatRow) #appends new matrix row to new matrix
    tranMatRow = [] #resets the matrix row variable

#loops through the rows of the transmuted matrix
for i in range(len(tranMat)):
    #loops through the columbs of the transmuted matrix
    for j in range(len(tranMat[0])):
        #prints the values of the matrix
        print(tranMat[i][j], end=" ")
    #formats the print
    print("\n", end="")
    
i = 0

#loops through i as long as it is within the row index
while i < rows:
    #loops through the columbs
    for j in range(colms):
        
        #gets the sum of the matrix rows multiplication
        matSum += matrix[i][j] * tranMat[v][k]
        
        #increments the v counter variable
        v += 1
    
    #increments the k counter
    k += 1
    #resets the v counter
    v = 0
    
    #checks if the k counter is out of the index range for the transmuted matrix
    if k != len(tranMat[0]):
        #resets i counter
        i -= 1
    else:
        #resets the k counter
        k = 0
    
    #increments the i counter
    i += 1
    
    matFin.append(matSum) #adds the sum to the finished matrix row
    
    if len(matFin) == len(tranMat[0]):
        #adds the finished row to the multiplied matrix
        multMat.append(matFin)
        #resets matrix row variable
        matFin = []
    #resets the summed variable
    matSum = 0


i = 0 #resets the i counter variable
j = 0 #resets the j counter variable

print() #formatting print

#loops through the rows of the multiplied matrix
for i in range(len(multMat)):
    #loops through the multiplied matrix columbs
    for j in range(len(multMat[0])):
        #prints the multiplied matrix
        print(multMat[i][j], end=" ")
    #goes to the next line
    print("\n", end="") 

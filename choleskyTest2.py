
# Online Python - IDE, Editor, Compiler, Interpreter

import numpy as np
from math import sqrt
    
def cholesky(A):
    # Given matrix A, Return matrix L a lower triangular cholesky decomp diamatrix
    # Get the dimensions of A
    n = A.shape[0]

    # Create zero matrix for L, make sure to set the data type as float
    L = np.zeros_like(A, dtype=float)

    # Perform a Cholesky decomp
    for i in range(n):
        for k in range(i+1):
            temp = sum(L[i][j] * L[k][j] for j in range(k))
            if (i == k): 
                value = A[i][i] - temp
                # In case the value gets too small
                if value >= 0:
                    L[i][k] = sqrt(value)
                else:
                    L[i][k] = 0
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - temp))
    return L
    
# For n = 4, ..., 15    
n = 4
while n <= 15:
    # Construct A, where aij = 1/(i+j-1)
    dim = n
    A = np.zeros((dim,dim),dtype=float)
    for i in range(n):
        for j in range(n):
            A[i][j] = 1 / ((i+1)+(j+1)-1)
    # Construct x, a vector of ones with the same dimensions as A
    x = np.ones((dim, 1))
    
    # Calculate b, the product of A and x
    b = A@x 
    
    # Calculate the Cholesky decomp
    R = cholesky(A)
    
    # Find the 2 norm of x - b and x
    numer = np.linalg.norm((x - b), 2)
    denom = np.linalg.norm(x, 2)
    
    # Find the error of the 2 norms
    error = numer/denom
    
    print("The n is", dim)
    print("The error is", error)
    n = n + 1
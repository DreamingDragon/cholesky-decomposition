
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
                L[i][k] = sqrt(A[i][i] - temp)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - temp))
    return L
n = 20
while n <= 100:
    # Construct A, a diagnal matrix with 4 on the main and 1 on the upper and lower co with an adjustable n value
    dim = n
    diamatrix = np.full((1,dim), 4)
    codiamatrix = np.full((1,dim-1), 1)
    diaflatM = np.diagflat(diamatrix)
    udiaflatM = np.diagflat(codiamatrix, 1)
    ldiaflatM = np.diagflat(codiamatrix, -1)
    A = diaflatM + udiaflatM + ldiaflatM
    
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
    n = n + 20
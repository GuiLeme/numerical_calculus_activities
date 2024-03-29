import numpy as np
from numerical_tools import (triangularize,
                             gauss_elimination_method)


# -----------------------------
# item number 1
# -----------------------------

# function f asked:
def f(x, k):
    return x**((2*k)-1)

# function to calculate integral:
def trapezoidal_rule(f, a, b, h, k):
    n = int((b-a)/h)
    x = np.linspace(a, b, n+1)
    y = f(x, k)
    T = (h/2) * (y[0] + 2*np.sum(y[1:n]) + y[n])
    return T

a = 0
b = 1
s = 5

# printing values:
# for k in range(3, 10):
#     m = s*(2**(k-1))
#     h = (b-a)/m
#     for i in range(0,k):
#       v = (2**i)
#       Th = trapezoidal_rule(f, a, b, v*h, k)
#       print(f"k = {k}: T({v:}h) = {Th:}")
#     print("-------------")



# -----------------------------
# item number 2
# -----------------------------


A = [[1,        1,      1       ], 
     [4,        16,     2**6    ], 
     [16,       256,    4**6    ]]

y = [1,         1,      1       ]

A_triangular, y_triangular = triangularize(A, y, 3)

print("Superior triangular matrix:")
for i in range(len(A_triangular)):
    print(A_triangular[i])
print("Independent terms vector:")
print(y_triangular)

print("---------------")

x = gauss_elimination_method(A, y, 3)

print("Final result for the example matrix:", x)

# Now, for each of the K's in the exercise's statement, we've got:

for k in range(3, 10):
    m = s*(2**(k-1))
    h = (b-a)/m
    independent_terms = []
    for i in range(0,k):
        v = (2**i)
        Th = trapezoidal_rule(f, a, b, v*h, k)
        Eh = Th - 1
        independent_terms.append(Eh)
    # Building the Matrix:
    Matrix = []
    for i in range(k):
        line = []
        i+=1
        for j in range(k):
            j+=1
            line.append((2**(i-1))**(2*j))
        Matrix.append(line)
    
    print(Matrix)
    
    x = gauss_elimination_method(Matrix, independent_terms, k)  
    
    print(x)  
    
    print("-------------")

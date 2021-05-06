# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 19:24:27 2021

@author: ANIL
"""

# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
  
# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
  

res = []

for x in range(len(A)):
    mulList = []
    i = 0
    for j in range(len(A[0])):
        sum1 = 0
        for k in range(len(B)):
            sum1 += (A[j][x] * B[k][j])
        mulList.append(sum1)
    res.append(mulList)
    
print(res)


# result will be 3x4
result = [[sum(a * b for a, b in zip(A_row, B_col)) 
                        for B_col in zip(*B)]
                                for A_row in A]
  
for r in result:
    print(r)
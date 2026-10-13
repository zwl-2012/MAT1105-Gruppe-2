##### Matrices #####
##### Packages #####
import numpy as np

print("\n---------- MAT1105 MATRICES ----------\n")

########## Initiate matrices ##########
A = np.array([[1,2,3,4], [5,6,7,8]])                    # 2x4 matrix
#print(A)
print(A.shape)                                          # (2, 4)

B = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])   # 4x3 matrix
#print(B)
print(B.shape)                                          # (4, 3)




########## Matrix multiplication ##########
AB = A @ B                                              # 2x3 matrix



########## Transpose ##########
A_T = np.transpose(A)                                   # 4x2 matrix




########## Inverse of a matrix ##########
C = np.array([[2,0,1], [3,0,0], [5,1,1]])               # 3x3 matrix

det_C = np.linalg.det(C)                                # determinant of C
inv_C = np.linalg.inv(C)                                # inverse of C
print(C @ inv_C)                                        # 3x3 identity matrix




########## Non-invertible ##########
D = np.array([[1,2,3], [0,2,2], [1,4,5]])               # 3x3 matrix

det_D = np.linalg.det(D)                                # determinant of D




########## Matrix addition/subtraction ##########
print(C + D)                                            # addition
print(C - D)                                            # subtraction

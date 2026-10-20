# Motivation and applications with matrices and matrix operations #

Explore some cases where matrix operations are used. In this case we are exploring mapping from one grid to another grid. 
Following topics are explored: 
- Setting up systems of equations as matrices
- Using Gaussian elimination to solve multiple systems simultaneously
- Finding the inverse of a matrix using MATLAB
- Python

---------------------

Step-by-step idea: 
1. Find the three coordinates from the original image grid (*image_box.jpg* or *dice.jpg*) (x1,y1), (x2,y2), (x3,y3)
   and the three new coordinates in the new grid (x1',y1'), (x2',y2'), (x3',y3'), such that it satisfies the transformations
   
   T(x1,y1,1) = (x1',y1',1), T(x2,y2,1) = (x2',y2',1) and T(x3,y3,1) = (x3',y3',1)
   
   where T = [a0 a1 a2; b0 b1 b2; 0 0 1] and
   
   a0\*x + a1\*y + a2 = x'

   b0\*x + b1\*y + b2 = y'
   
3. Set up the system of equations
   
5. Use Gaussian elimination to get the coefficients a0,a1,a2,b0,b1,b2

6. Find the inverse of T

7. Do inverse mapping to transform the image grid

---------------------

Files: 

**mapping_1.py**: File containing mapping of *image_box.jpg*

**mapping_2.py**: File containing mapping of *dice*


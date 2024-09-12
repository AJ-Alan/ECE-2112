# Programming Assignment 2: Numerical Python (Numpy)

** **

**Normalization Problem**\
*Description:*\
  create a random 5 x 5 ndArray, normalize the array, then save it\
*Solution:*
  1. Makes use of the random array function: X = np.random.random.((5,5))
  2. Uses the .mean() and .std() functions to find their respective values in  array X, then using the normalization formula using these values to create an array Z with all the normalized values
  3. using the np.save() function to save the array Z
  4. prints the saved array to confirm if its saved properly\

*Code:*\
`#create a random 5 x 5 ndArray named X`\
`X = np.random.random((5,5))`\
`#normalize the values of each and every value of the array`\
`Z = (X - X.mean())/(X.std())`\
`#save the array as a python file`\
`np.save('X_normalized',Z)`\
`#view the values of the arrays`\
`print("Array:\n",X,"\n\nNormalized Array:\n",np.load('X_normalized.npy'))`

Normalized Array in file:
 [[ 0.76232056 -1.32638324  1.50481777  1.33541675  1.68454132]
 [-1.52043894 -1.3794231  -0.40017018  0.53489377 -0.12055061]
 [-1.4809231   0.7823328  -0.90030017  1.12804484 -0.14042066]
 [-0.19968605  0.82724207 -0.95593837  0.66485551 -0.37415949]
 [ 0.25073711 -1.22076226 -0.91289345  0.21701334  1.2398338 ]]


** **
  
**Divisible by 3 Problem**\
*Description:*\
  create a 10 x 10 array of squared values from 1 - 100 and create a new array with all values that are divisible by 3\
*Solution:*
  1. First create a list with 1 as the value to initiliaze array A
  2. Use a for loop with variable x and range from 2 to 101, then appends the square of x to the list
  3. using the function np.array() function to change list A into an array and then using the .reshape() function to change it to a 10 x 10 array
  4. using the np.save() function to save the array A

# Programming Assignment 2: Numerical Python (Numpy)

** **

**Normalization Problem**\
*Description:*\
  create a random 5 x 5 ndArray, normalize the array, then save it\
*Solution:*
  1. Makes use of the random array function: X = np.random.random.((5,5))
  2. Uses the .mean() and .std() functions to find their respective values in  array X, then using the normalization formula using these values to create an array Z with all the normalized values
  3. using the np.save() function to save the array Z
  4. prints the saved array to confirm if its saved properly

*Code:*\
`#create a random 5 x 5 ndArray named X`\
`X = np.random.random((5,5))`\
`#normalize the values of each and every value of the array`\
`Z = (X - X.mean())/(X.std())`\
`#save the array as a python file`\
`np.save('X_normalized',Z)`\
`#view the values of the arrays`\
`print("Array:\n",X,"\n\nNormalized Array:\n",np.load('X_normalized.npy'))`

*Results:*\
Array X:\
`[[0.94488476 0.26294944 0.99176034 0.62708767 0.86468772]`\
` [0.45125235 0.24217754 0.26118995 0.94754924 0.7665089 ]`\
` [0.37212077 0.16627127 0.67809948 0.42834649 0.91753308]`\
` [0.86881849 0.22781775 0.67933033 0.04151736 0.7174865 ]`\
` [0.28670169 0.82858137 0.65424129 0.80518701 0.26510077]]`

Normalized Array Z in file 'X_normalized.npy':\
`[[ 1.29395421 -1.07173184  1.45656921  0.19149169  1.01574452]`\
` [-0.41849457 -1.14379115 -1.07783566  1.3031975   0.67515466]`\
` [-0.69300809 -1.40711584  0.36845559 -0.49795674  1.19906915]`\
` [ 1.03007449 -1.19360636  0.37272547 -1.83989676  0.50509217]`\
` [-0.98933345  0.89048882  0.28568969  0.809332   -1.06426872]]`

** **
  
**Divisible by 3 Problem**\
*Description:*\
  create a 10 x 10 array of squared values from 1 - 100 and create a new array with all values that are divisible by 3\
*Solution:*
  1. First create a list with 1 as the value to initiliaze array A
  2. Use a for loop with variable x and range from 2 to 101, then appends the square of x to the list
  3. using the function np.array() function to change list A into an array and then using the .reshape() function to change it to a 10 x 10 array
  4. using the np.save() function to save the array A

*Code:*\
`#create a base list for the values `\
`A = [1]`\
`#loop that will insert the squared values`\
`for x in range(2, 101): `\
`    A.append(x*x)`\
`#changes list into an 10 x 10 array`\
`A = np.array(A)`\
`A.reshape(10,10)`\
`#determines the elements that are divisible by 3`\
`Z = A[A%3==0]`\
`#save the array as a python file`\
`np.save('div_by_3',Z)`\
`#view the values of the arrays`\
`print("Array:\n",A,"\n\nDivisible by 3 values from A:\n",np.load('div_by_3.npy'))`\

*Results:*\
Array A:\
`[    1     4     9    16    25    36    49    64    81   100   121   144`\
`   169   196   225   256   289   324   361   400   441   484   529   576`\
`   625   676   729   784   841   900   961  1024  1089  1156  1225  1296`\
`  1369  1444  1521  1600  1681  1764  1849  1936  2025  2116  2209  2304`\
`  2401  2500  2601  2704  2809  2916  3025  3136  3249  3364  3481  3600`\
`  3721  3844  3969  4096  4225  4356  4489  4624  4761  4900  5041  5184`\
`  5329  5476  5625  5776  5929  6084  6241  6400  6561  6724  6889  7056`\
`  7225  7396  7569  7744  7921  8100  8281  8464  8649  8836  9025  9216`\
`  9409  9604  9801 10000] `\

Array Z in file 'div_by_3.npy':\
` [   9   36   81  144  225  324  441  576  729  900 1089 1296 1521 1764`\
` 2025 2304 2601 2916 3249 3600 3969 4356 4761 5184 5625 6084 6561 7056`\
` 7569 8100 8649 9216 9801]`\


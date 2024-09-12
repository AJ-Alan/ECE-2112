# Programming Assignment 2: Numerical Python (Numpy)

**Normalization Problem**\
*Description:*
  create a random 5 x 5 ndArray, normalize the array, then save it\
*Solution:*
  1. Makes use of the random array function: X = np.random.random.((5,5))
  2. Uses the .mean() and .std() functions to find their respective values in  array X, then using the normalization formula using these values to create an array Z with all the normalized values
  3. using the np.save() function to save the array Z
  4. prints the saved array to confirm if its saved properly
  
**Divisible by 3 Problem**
*Description:*
  create a 10 x 10 array of squared values from 1 - 100 and create a new array with all values that are divisible by 3\
*Solution:*
  1. First create a list with 1 as the value to initiliaze array A
  2. Use a for loop with variable x and range from 2 to 101, then appends the square of x to the list
  3. using the function np.array() function to change list A into an array and then using the .reshape() function to change it to a 10 x 10 array
  4. using the np.save() function to save the array A

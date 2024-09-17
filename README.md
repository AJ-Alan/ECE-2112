# Programming Assignment 3: Python Data Analysis (Pandas)

**Problem 1: Five and Five Cars**\
*Description:*\
&emsp;Using new Pandas knowledge to solve pandas displaying problems with the given 'cars.csv':
1. Load "cars.csv" into a data frame named "dfCars" using pandas
2. Display the first five and last five rows of the resulting cars
3. Save as a .py file named "Villarmil_Pandas-P1.py"

*Solution:*
  1. First import pandas library
  2. Next, initiliaze variable 'dfCars' as the 'cars.csv' dataframe using the pd.read_csv()
  3. Then display the first five and last five rows of dfCars using the .loc() function with the parameters of checking the dfCars.index if its less than 5 or more than the 6 less the max index `dfCars.index>(dfCars.index.stop-6)`, which precisely shows the first five and last five rows of the data frame
  4. Lastly, save the code as "Villarmil_Pandas-P1.py"

*Results:*\
`       Model                mpg	cyl	disp	hp	drat	wt	qsec	vs	am	gear	carb`\
`0	Mazda RX4	    21.0	6	160.0	110	3.90	2.620	16.46	0	1	4	4`\
`1	Mazda RX4 Wag	    21.0	6	160.0	110	3.90	2.875	17.02	0	1	4	4`\
`2	Datsun 710	    22.8	4	108.0	93	3.85	2.320	18.61	1	1	4	1`\
`3	Hornet 4 Drive	    21.4	6	258.0	110	3.08	3.215	19.44	1	0	3	1`\
`4	Hornet Sportabout    18.7	8	360.0	175	3.15	3.440	17.02	0	0	3	2`\
`28	Ford Pantera L	    15.8	8	351.0	264	4.22	3.170	14.50	0	1	5	4`\
`29	Ferrari Dino	    19.7	6	145.0	175	3.62	2.770	15.50	0	1	5	6`\
`30	Maserati Bora	    15.0	8	301.0	335	3.54	3.570	14.60	0	1	5	8`\
`31	Volvo 142E	    21.4	4	121.0	109	4.11	2.780	18.60	1	1	4	2`

** **
  
**Problem 2: Searching Characteristics**\
*Description:*\
&emsp;With the same dataframe, use subsetting, slicing, and indexing operations to find the following:
1. Display the first five rows with odd-numbered columns of cars
2. Display the row that contains the 'Model' of 'Mazda RX4'
3. Find how many cylinders does the car model 'Camaro Z28' have
4. Determine the number of cylinders and gear types of the car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'
5. Then save as a .py file named "Villarmil_Pandas-P2.py"

*Solution:*
1. To display the first five rows with odd-numbered columns:
>Using the .loc() function with the conditions of checking if the indices of dfCars is less than 10 and if its modulus of 2 is equal to 1 (which refers to all odd numbers)
2. To display the row that contains the 'Model' of Mazda RX4':
>Using the .loc() function to check all rows of column 'Model' if they have the model 'Mazda RX4' and displays all the characteristics of that model
3. To find how many cylinders does the car model 'Camaro Z28' have:
>Using the .loc() function to first find the model 'Camaro Z28', then the only columns to display are 'Model' and 'cyl' to show the cylinder count and which model it belongs to (to be explicit)
4. To determine the cylinders and gear types of the car models of 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic':
>Using the .loc() function to find the models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' then the only columns to display are 'Model', 'cyl', and 'gear' to show the cylinders and gears of the respective models
5. Using the print() function so they could all print in one .py file


*Results:*\
# for 1.
# 	    Model	        mpg	    cyl	    disp	hp	    drat	wt	    qsec	vs	am	gear	carb
# 1	    Mazda RX4 Wag	21.0	6	    160.0	110	    3.90	2.875	17.02	0	1	4	    4
# 3	    Hornet 4 Drive	21.4	6	    258.0	110	    3.08	3.215	19.44	1	0	3	    1
# 5	    Valiant	        18.1	6	    225.0	105	    2.76	3.460	20.22	1	0	3	    1
# 7	    Merc 240D	    24.4	4	    146.7	62	    3.69	3.190	20.00	1	0	4	    2
# 9	    Merc 280	    19.2	6	    167.6	123	    3.92	3.440	18.30	1	0	4	    4

# for 2.
#   Model	    mpg	    cyl     disp	hp	    drat	wt	    qsec	vs	am	gear	carb
# 0	Mazda RX4	21.0	6	    160.0	110 	3.9	    2.62	16.46	0	1	4	    4

# for 3. (I have decided to show the model alongside to what is asked because it is not explicit as to which model is being shown since the questions are not displayed)
# 	    Model	    cyl
# 23	Camaro Z28	8

# for 4.
# 	    Model	        cyl     gear
# 1	    Mazda RX4 Wag	6	    4
# 18	Honda Civic	    4	    4
# 28	Ford Pantera L	8	    5



** **

Version History:\
**V0.1:** - initial upload\
**V0.2:** - in Villarmil_Pandas-P1.py, changes static comparison `(dfCars.index>26)` to `(dfCars.index>(dfCars.index.stop-6))` to have a more dynamic comparison that works even with other dataframes to always show the first five and last five rows of the dataframe.\
**V0.3** - added the results as comments inside the files themselves
**V0.4** - added note that the displayed results will not have perfect indention

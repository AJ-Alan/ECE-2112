import pandas as pd #import pandas
dfCars = pd.read_csv('cars.csv') #reads the file 'cars.csv' and inserts to variable 'dfCars'

#1. display the first five rows with odd-numbered columns of cars
print(dfCars.loc[(dfCars.index<10)&(dfCars.index%2==1)]) #checks first ten rows and checks if their modulus is equal to 1 (which is for odd numbers)

#2. Display the row that contains the 'Model' of 'Mazda RX4'
print(dfCars.loc[dfCars['Model']=='Mazda RX4',]) #checks all rows of column 'Model' if they have the model 'Mazda RX4'

#3. Find how many cylinders does the car model 'Camaro Z28' have
print(dfCars.loc[dfCars['Model']=='Camaro Z28',['Model','cyl']]) #displays the model and how many cylinders does it have (it has 8)

#4. Determine the number of cylinders and gear types of the car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'
print(dfCars.loc[(dfCars['Model']=='Mazda RX4 Wag')|(dfCars['Model']=='Ford Pantera L')|(dfCars['Model']=='Honda Civic'),['Model','cyl','gear']]) #checks those that have the same models as the question and the following column characteristics

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


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
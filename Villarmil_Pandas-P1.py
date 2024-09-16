import pandas as pd #import pandas
dfCars = pd.read_csv('cars.csv') #reads the file 'cars.csv' and inserts to variable 'dfCars'
dfCars.loc[(dfCars.index<5)|(dfCars.index>26)] #displays the first five rows and the last five rows of the dataframe
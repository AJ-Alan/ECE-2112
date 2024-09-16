import pandas as pd #import pandas
dfCars = pd.read_csv('cars.csv') #reads the file 'cars.csv' and inserts to variable 'dfCars'
print(dfCars.loc[(dfCars.index<5)|(dfCars.index>(dfCars.index.stop-6))]) #displays the first five rows and the last five rows of the dataframe

#Results:

#       Model                mpg    cyl	    disp	hp	    drat	wt	    qsec	vs	am	gear	carb
# 0	    Mazda RX4	        21.0	6	    160.0	110	    3.90	2.620	16.46	0	1	4	    4
# 1	    Mazda RX4 Wag	    21.0	6	    160.0	110	    3.90	2.875	17.02	0	1	4	    4
# 2	    Datsun 710	        22.8	4	    108.0	93	    3.85	2.320	18.61	1	1	4	    1
# 3	    Hornet 4 Drive	    21.4	6	    258.0	110	    3.08	3.215	19.44	1	0	3	    1
# 4	    Hornet Sportabout   18.7	8	    360.0	175	    3.15	3.440	17.02	0	0	3	    2
# 28	Ford Pantera L	    15.8	8	    351.0	264	    4.22	3.170	14.50	0	1	5	    4
# 29	Ferrari Dino	    19.7	6	    145.0	175	    3.62	2.770	15.50	0	1	5	    6
# 30	Maserati Bora	    15.0	8	    301.0	335	    3.54	3.570	14.60	0	1	5	    8
# 31	Volvo 142E	        21.4	4	    121.0	109	    4.11	2.780	18.60	1	1	4	    2

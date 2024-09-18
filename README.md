# Programming Assignment 4: Data Wrangling and Data Visualization

**ECE Board Exam Problem:** <br>
Analyze the ECE Board Exam 2 dataset using data wrangling and data visualization techniques. <br>
1. Data Frames:
> a. Shows scores of GEAS and names of those who scored higher than 70 in Electronics where their track is Instrumentation and hometown is Luzon <br>
b. Shows scores in Electronics, names, and tracks of those who scored higher or equal to the average of 55 where their hometown is Mindanao and their gender is Female 

2. Data Visualization about how different features contribute to their average grade and asks the question of whether: track, gender, or hometown contributes to higher average score <br>

** **

# *Solution:* <br>
**Preparation:** <br>
1. Import relevant libraries: <br>
```Python
import pandas as pd #for data frames
import matplotlib.pyplot as plt #for data visualization (graphs)
import seaborn as sns #for data visualization (advanced)
```
2. Loads data frame 'board2.xlsx' as a variable using the pd.read_excel() function <br>
```Python
dfExam = pd.read_excel('board2.xlsx') #loads the ECE board exam scores as dfExam for the following problems
```
<br>

**Part 1: Data Frames** <br>
- Using the .loc[] function, the specific conditions that are asked for can be found with providing the conditions in the function<br>

<br>

**Results** <br>

Code for Part A:<br>
```Python
#scores of GEAS and names of those who scored higher than 70 in Electronics where their track is Instrumentation and hometown is Luzon
Instru = dfExam.loc[ #uses .loc function to find the conditions and equates the dataframe to Instru
    (dfExam['Electronics']>70)& #checks if the scores under Electronics is greater than 70
    (dfExam['Hometown']=='Luzon')& #and checks if the test takers' hometown is  Luzon
    (dfExam['Track'] == 'Instrumentation'), #then checks if their tracks are under Instrumentation
    ['Name','GEAS','Electronics']] #then these are the columns to be located in the dataframe
print(Instru) #prints out Instru
```

Output: <br>
![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/Instru.png?raw=true)
<br>
<br>
Code for Part B:<br>

```Python
Mindy = dfExam.loc[ #uses .loc function to find the conditions and equates the dataframe to Mindy
    (dfExam['Average']>=55)& #checks if the Average is 55 or higher
    (dfExam['Hometown'] == 'Mindanao')& #and checks if the test takers' hometown is Mindanao
    (dfExam['Gender'] == 'Female'), #then checks if the test takers' gender is female
    ['Name','Track','Electronics','Average']] #then these are the columns to be located in the dataframe
```
Output:<br>
![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/Mindy.png?raw=true)
<br>
** **
**Part 2: Data Visualization** <br>

To sort and display the data, the following functions were used: <br>
- **sns.boxplot(x,y,hue,data)** = function that creates a boxplot graph of the given data (as dataframe) with other inputs as x, y, and hue the data from columns of the given data frame<br>
- **plt.title(string)** = function used to provide a title to the graph with string as the input<br>
- **plt.show()** = function used to show the boxplot<br>
<br>

To edit the visuals of the data, the following functions were used:<br>
- **sns.set_style(preset)** = function that chooses from presets for the main colors <br>
- **sns.set_palette(list)** = function that takes from a list of hex colors as the palette for the graph<br>
<br>

**Results**<br>

Code: <br>

```Python
#...
sns.boxplot(x ='Track', y ='Average', hue ='Gender', data = dfExam)
plt.title('Correlation between Track with Gender and Average Grades')
plt.show()
#...
```
Output: <br>
![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/CorrelationTrackGender.png?raw=true)

Code: <br>
```Python
#...
sns.boxplot(x='Hometown', y='Average', hue='Track', data=dfExam)
plt.title('Correlation between Hometown with Track and Average Grades')
plt.show()
#..
```
Output: <br>
![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/CorrelationHometownTrack.png?raw=true)

Code: <br>
```Python
#...
sns.boxplot(x='Gender', y='Average', hue='Hometown', data=dfExam)
plt.title('Correlation between Gender with Hometown and Average Grades')
plt.show()
#...
```
Output: <br>
![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/CorrelationGenderHometown.png?raw=true)


**Version History** <br>
0.1 initial release <br>
0.1.1 minor edits to comments

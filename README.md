# Programming Assignment 4: Data Wrangling and Data Visualization

**ECE Board Exam Problem:**\
&emsp;Analyze the ECE Board Exam 2 dataset using data wrangling and data visualization techniques.\
&emsp;\
&emsp;1. Data Frames:
> a. Shows scores of GEAS and names of those who scored higher than 70 in Electronics where their track is Instrumentation and hometown is Luzon\
b. Shows scores in Electronics, names, and tracks of those who scored higher or equal to the average of 55 where their hometown is Mindanao and their gender is Female 

&emsp;2. Data Visualization about how different features contribute to their average grade and asks the question of whether: track, gender, or hometown contributes to higher average score <br>

** **

# *Solution:* <br>
**Part 1: Data Frames** <br>
```Python
Instru = dfExam.loc[ #uses .loc function to find the conditions and equates the dataframe to Instru
    (dfExam['Electronics']>70)& #checks if the scores under Electronics is greater than 70
    (dfExam['Hometown']=='Luzon')& #and checks if the test takers' hometown is  Luzon
    (dfExam['Track'] == 'Instrumentation'), #then checks if their tracks are under Instrumentation
    ['Name','GEAS','Electronics']] #then these are the columns to be located in the dataframe
```
![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/Instru.png?raw=true)
```Python
Mindy = dfExam.loc[ #uses .loc function to find the conditions and equates the dataframe to Mindy
    (dfExam['Average']>=55)& #checks if the Average is 55 or higher
    (dfExam['Hometown'] == 'Mindanao')& #and checks if the test takers' hometown is Mindanao
    (dfExam['Gender'] == 'Female'), #then checks if the test takers' gender is female
    ['Name','Track','Electronics','Average']] #then these are the columns to be located in the dataframe
```
![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/Mindy.png?raw=true)
<br><br><br>
** **
**Part 2: Data Visualization** <br>

To sort and display the data, the following functions were used: <br>
&emsp;**sns.boxplot(x,y,hue,data)** = function that creates a boxplot graph of the given data (as dataframe) with other inputs as x, y, and hue the data from columns of the given data frame<br>
&emsp;**plt.title(string)** = function used to provide a title to the graph with string as the input<br>
&emsp;**plt.show()** = function used to show the boxplot<br>
<br><br>
To edit the visuals of the data, the following functions were used:<br>
&emsp;**sns.set_style(preset)** = function that chooses from presets for the main colors <br>
&emsp;**sns.set_palette(list)** = function that takes from a list of hex colors as the palette for the graph<br>
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

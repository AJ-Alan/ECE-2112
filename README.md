# Programming Assignment 4: Data Wrangling and Data Visualization

**ECE Board Exam Problem:**\
&emsp;Analyze the ECE Board Exam 2 dataset using data wrangling and data visualization techniques.\
&emsp;\
&emsp;1. Data Frames:
> a. Shows scores of GEAS and names of those who scored higher than 70 in Electronics where their track is Instrumentation and hometown is Luzon\
b. Shows scores in Electronics, names, and tracks of those who scored higher or equal to the average of 55 where their hometown is Mindanao and their gender is Female 

&emsp;2. Data Visualization about how different features contribute to their average grade and asks the question of whether: track, gender, or hometown contributes to higher average score <br>

*Solution:* <br>
**Part 1: Data Frames** <br>
![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/Instru.png?raw=true)
![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/Mindy.png?raw=true)
**Part 2: Data Visualization** <br>


![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/CorrelationTrackGender.png?raw=true)

![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/CorrelationHometownTrack.png?raw=true)

![](https://github.com/AJ-Alan/ECE-2112/blob/PA4/CorrelationGenderHometown.png?raw=true)

Using plt.savefig() function to get the pictures of these data: <br>
```Python
#...
plt.savefig("CorrelationNAME1NAME2.png")
```

**Version History** <br>
0.1 initial release

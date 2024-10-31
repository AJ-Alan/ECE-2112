# An Explorative Data Analysis on Spotify's Dataset from 2023 
By Arc Joseph C. Villarmil, 2ECE-D <br>

**Description** <br>
>Describe what this is for
>analyze, visualize, and interpret the data to extract meaningful insights (replace)

**Regarding the Dataset and its contents** <br>
>Describe that this is for Spotify Dataset
>remember that the link is in the sources

<br>

## Before the Analysis 

**Importing the necessary libraries** <br>
```Python
import numpy as np #imports numpy library for number and array manipulation
import pandas as pd #imports pandas library for data analysis and wrangling
import matplotlib.pyplot as plt #imports matplotlib for data plot creation
import seaborn as sns #imports seaborn to create visually appealing data plots
```

**Viewing the Dataset** <br>
The CSV file was loaded into a Python dataframe named 'dataSpotify' using this code: <br>
```Python
dataSpotify = pd.read_csv("spotify-2023.csv", encoding = 'latin-1')
```
Due to an encoding error that essentially needs this code ``encoding='latin-1')`` for it to load <br>
The data can be viewed but due to its large size, some data is cut off in Python and the full data is too large to be viewed here on the documentation, hence it needs to be summarized and simplified to understand the data better <br>
<br>
In dataSpotify, the .describe() function was used to find if it could be used for this problem, <br>
![](https://github.com/AJ-Alan/ECE-2112/blob/An-Explorative-Data-Analysis-on-Spotify's-Dataset-from-2023/descData.png)
<br>
As seen here, there are a few data points that are of interest, those being: (change to list) the count, measures of position for years, number of columns, statistics of the streams column... (check more wait Im gonna save for now)

<br>

## Statistics

**Overview of Dataset** <br>
>How many rows and columns does the dataset contain?
>What are the data types of each column? Are there any missing values?

**Basic Descriptive Statistics** <br>
>What are the mean, median, and standard deviation of the streams column?
>What is the distribution of released_year and artist_count? Are there any noticeable trends or outliers?

**Top Performers** <br>
>Which track has the highest number of streams? Display the top 5 most streamed tracks.
>Who are the top 5 most frequent artists based on the number of tracks in the dataset?

**Temporal Trends** <br>
>Analyze the trends in the number of tracks released over time. Plot the number of tracks released per year.
>Does the number of tracks released per month follow any noticeable patterns? Which month sees the most releases?

**Genre and Music Characteristics** <br>
>Examine the correlation between streams and musical attributes like bpm, danceability_%, and energy_%. Which attributes seem to influence streams the most?
>Is there a correlation between danceability_% and energy_%? How about valence_% and acousticness_%?

**Platform Popularity** <br>
>How do the numbers of tracks in spotify_playlists, spotify_charts, and apple_playlists compare? Which platform seems to favor the most popular tracks?

<br>

## Data Analysis

**Correlations of Data** <br>
>Investigate correlations between different variables and provide insights based on your findings. Explore relationships between streams and other musical characteristics like tempo, energy, or playlists.
>Based on your analysis, offer any insights or recommendations regarding the tracks, artists, or musical trends tat could be useful for understanding what makes a track popular.

**Observations Regarding the Data (Advanced Analysis)** <br>
> Based on the streams data, can you identify any patterns among tracks with the same key or mode (Major vs. Minor)?
> Do certain genres or artists consistently appear in more playlists or charts? Perform an analysis to compare the most frequently appearing artists in playlists or charts.

**Recommendations**<br>
>Last part after all the analysis and provide recommendations regarding the tracks, artists, or musical trends that could be useful for understanding what makes a track popular.

<br>

**Version History** <br>
10/30/2024 <br>
0.0: Initial Creation <br>
0.0.1: Creation of README.md, Notebook, and uploading of CSV file for reference <br>
0.0.2: Finalized outline for the README.md
10/31/2024 <br>
0.1: Began to document the initial analysis and created a Formal Notebook and a Test Notebook 
0.1.1: Added code and images relating to the "Before the Analysis" section in the README file

<br>

**Sources:** <br>
Elgiriyewithana, N. (2023). *Most Streamed Spotify Songs 2023* [Data set]. Kaggle. [https://doi.org/10.34740/kaggle/dsv/6367938](https://doi.org/10.34740/kaggle/dsv/6367938) <br>


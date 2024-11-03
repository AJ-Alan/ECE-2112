# An Explorative Data Analysis on Spotify's Dataset from 2023 
By Arc Joseph C. Villarmil, 2ECE-D <br>

**Table of Contents**: <br>
[Before the Analysis](#Before-the-Analysis)

** **

*Description*: <br>
<br>
This is a Data Analysis on Spotify's most streamed songs during 2023. The aim of this analysis is to understand the dataset that's available online using Python, not only for its powerful use in analysis but to deepen one's knowledge in how to use the Python Programming Language. The following sections will analyze, visualize, and interpret Spotify's data to extract meaningful insights that can be used for recommendations to understand what makes a track popular. <br> 
<br>

*Regarding the Dataset and its contents*: <br>
<br>
The Spotify Dataset contains a plethora of data such as the track name, artist(s) name, release date, Spotify playlists and charts, streaming statistics, Apple Music presence, Deezer presence, Shazam charts, and various audio features. All of these data comes from the most famous songs of 2023 that were listed on Spotify. This came from Nidula Elgiriyewithana on kaggle who posted it a year ago on Kaggle. The link to the source is in the **Sources** section at the bottom of this file (Elgiriyewithana, 2023).

<br>

## Before the Analysis 

**Importing the necessary libraries** <br>
```Python
import numpy as np #imports numpy library for number and array manipulation
import pandas as pd #imports pandas library for data analysis and wrangling
import matplotlib.pyplot as plt #imports matplotlib for data plot creation
import seaborn as sns #imports seaborn to create visually appealing data plots
```
<br>

**Viewing the Dataset** <br>
The CSV file was loaded into a Python dataframe named 'dataSpotify' using this code: <br>
```Python
dataSpotify = pd.read_csv("spotify-2023.csv", encoding = 'latin-1')
```
Due to an encoding error that essentially needs this code ``encoding='latin-1')`` for it to load <br>
The data can be viewed but due to its large size, some data is cut off in Python and the full data is too large to be viewed here on the documentation, hence it needs to be summarized and simplified to understand the data better <br>
<br>
In dataSpotify, the ```.describe()``` function was used to find if it could be used for this problem, <br>
![](https://github.com/AJ-Alan/ECE-2112/blob/An-Explorative-Data-Analysis-on-Spotify's-Dataset-from-2023/descData.png)
<br>
As seen here, there are a few data points that are of interest, those being: 
* count of songs
* measures of position for years
* number of columns
* the statistics of the streams column
<br>

Further analysis will require detailed documentation and coding. <br>
As such, the following sections will be for this purpose. <br>
* **Summary of Statistics** will summarize various statistics relevant to the data frame.
* **Data Analysis** will analyze the results of the statistics and provide relevant recommendations.
* **Version History** will provide a version history for this Data Analysis
* **Sources** will provide the sources that were used for this Data Analysis

<br>

** **

<br>

## Summary of Statistics

**Overview of Dataset** <br>

<br>

Using the ```.shape``` attribute to dataSpotify,
```Python
dataSpotify.shape #results to a tuple of (rows, columns)
#the result should be (953,24)
```
This results to:
* 953 rows
* 24 columns
These values can be inferred from the ```.describe()``` function, although its not specific as it only counts the number of songs and doesn't show the number of columns.

<br>
The 953 rows refers to how many songs are in the dataset, and the 24 columns refer to the "Key Features" of each song. These Key Features include: <br>

* track_name: Name of the song
* artist(s)_name: Name of the artist(s) of the song
* artist_count: Number of artists contributing to the song
* released_year: Year when the song was released
* released_month: Month when the song was released
* released_day: Day of the month when the song was released
* in_spotify_playlists: Number of Spotify playlists the song is included in
* in_spotify_charts: Presence and rank of the song on Spotify charts
* streams: Total number of streams on Spotify
* in_apple_playlists: Number of Apple Music playlists the song is included in
* in_apple_charts: Presence and rank of the song on Apple Music charts
* in_deezer_playlists: Number of Deezer playlists the song is included in
* in_deezer_charts: Presence and rank of the song on Deezer charts
* in_shazam_charts: Presence and rank of the song on Shazam charts
* bpm: Beats per minute, a measure of song tempo
* key: Key of the song
* mode: Mode of the song (major or minor)
* danceability_%: Percentage indicating how suitable the song is for dancing
* valence_%: Positivity of the song's musical content
* energy_%: Perceived energy level of the song
* acousticness_%: Amount of acoustic sound in the song
* instrumentalness_%: Amount of instrumental content in the song
* liveness_%: Presence of live performance elements
* speechiness_%: Amount of spoken words in the song

<br>

These descriptions of the Key Features come from the Kaggle source (Elgiriyewithana, 2023).

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

## Version History
10/30/2024 <br>
0.0: Initial Creation <br>
0.0.1: Creation of README.md, Notebook, and uploading of CSV file for reference <br>
0.0.2: Finalized outline for the README.md <br>
10/31/2024 <br>
0.1: Began to document the initial analysis and created a Formal Notebook and a Test Notebook <br>
0.1.1: Added code and images relating to the "Before the Analysis" section in the README file <br>
11/1 ~ 11/2 were spent visiting deceased loved ones <br>
11/3/2024 <br>
0.1.2: Further continued the documentation, started the summary of statistics, made some edits, and added more to the Formal Notebook

<br>

## Sources:
Elgiriyewithana, N. (2023). *Most Streamed Spotify Songs 2023* [Data set]. Kaggle. [https://doi.org/10.34740/kaggle/dsv/6367938](https://doi.org/10.34740/kaggle/dsv/6367938) <br>


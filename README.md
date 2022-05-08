# Surfs_Up

## Project Overview

The client is looking for a weather analysis to determine if the new Surf and Shake shop is a viable business to run all year long on the island of Oahu. The investors provided the weather dataset that the analysis is being performed including the breakdown of precipitation and temperatures all year. A list of deliverables is highlighted below as per the investor's requirements.

1.	You can retrieve and plot the last year's precipitation data by querying the dataset.Find the most active weather station.
2.	The data for the last 12 months of temperature observation can be retrieved and plotted.
3.	Create a dataframe of the results with specific filtering for the months of June and December.
4.	The precipitation data and temperature data should be summarized using the count, mean, standard deviation, minimum, maximum, and 25/50/75 quartiles.

## Resources

•	Data Source: hawaii.sqlite

•	Software: Python 3.9.7, Anaconda 2021.03, Jupyter Notebook 6.4.5,  VS Code version 1.67.0

## Results

![June_Temps](https://user-images.githubusercontent.com/99752443/167279683-2e3f783a-3d53-4410-a0cf-a0120542ba6c.png)


![December_Temps](https://user-images.githubusercontent.com/99752443/167279685-a7fe57d8-9dd9-42ef-8773-37bde33b2d62.png)


•	Oahu's summer and winter commence at different intervals, with the average temperature difference between the two opposite months not greatly different at 74 degrees in the summer and 71 degrees in the winter.The median for December's temperature is 71 degrees while the Summer's median is 75 degrees farenheit, it can be safely assumed that although the difference isnt drastic like stated in the first argument, there will be more slower days during the winter especially if half of the time the temperatures fall below 71 degrees.

•	If we examine one of the 'worst' weather conditions strictly from the perspective of temperature, it is safe to assume that 25% of the time during December it will be a slower day since the temperatures fall below 69 degrees.degrees farenheit. Different sets of data including precipitation has to be analyzed in order to solidify this statement. Nonetheless it is a good starting point for an assumption.


## Summary

Despite the fact that this particular analysis heavily focused on the opposing seasons of summer and winter, the preliminary investigation shows that the temperature differences between the two are pretty similar, so, in theory, there won't be a substantial drop-off in sales. Nonetheless, further research could be done to facilitate the decision of the investors, particularly by looking at the average precipitation for each month. In spite of similar temperatures, precipitation might keep tourists away in a particular month, resulting in less business. With the given dataset, another query that could be performed is finding the low and high rates of precipitation on the island for a particular month by filtering precipitation rates by the weather station. An observation location for each station is indicated in the 'station' table of the dataset. A more comprehensive dataset should include tourist numbers, further weather analysis like humidity and cloud coverage, and further data on precipitation and temperature rates.


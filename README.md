# **<p align="center">Surfs Up!</p>**

### **<p align="center">A Python-powered analytics report designed to display Temperature statistics for the island of Oahu.</p>**

---
## Overview
This report will display a statistical analysis of the Temperature of the island of Oahu in the months of June and December. This information will be used to determine if Oahu is a viable location for a Surf and Ice Cream shop. In the Results section below is our analysis results for both months. Following that is the Summary section where additional queries are suggested and our conclusions are presented.

---
## **<p align="center">Results - June Temperatures</p>**
---

<p align="center">
   <img width="200" height="275" src="https://github.com/Jamesrx33/Surfs-Up/blob/main/Resources/June_Statistics.png?raw=true">
</p>

1. **Average Temp:** Out of 1700 recorded temperatures, the average temp was 74.9 degrees Fahrenheit.
2. **Minimum Temp:** The minimum temperature was 64 degrees Fahrenheit.
3. **Maximum Temp:** The maximum temperature was 85 degrees Fahrenheit.
4. **% over 70:** At least 75% of the temperatures in the month of June were over 70 degrees Fahrenheit.
 
---
## **<p align="center">Results - December Temperatures</p>**

<p align="center">
   <img width="200" height="275" src="https://github.com/Jamesrx33/Surfs-Up/blob/main/Resources/December_Statistics.png?raw=true">
</p>

---

1. **Average Temp:** Out of 1517 recorded temperatures, the average temp was 71 degrees Fahrenheit.
2. **Minimum Temp:** The minimum temperature was 56 degrees Fahrenheit.
3. **Maximum Temp:** The maximum temperature was 83 degrees Fahrenheit.
4. **% over 70:** At least 50% of the temperatures in the month of December were over 70 degrees Fahrenheit.

---
## Summary
---

The island of Oahu appears to be warm and temperate nearly year round. June, the middle of Summer, never exceeds 85 degrees Fahrenheit with at least 75% of the temperatures over 70. December, the middle of Winter, gets as hot as 83 degrees Fahrenheit with at least 50% of the temperatures over 70. This indicates that Oahu, on average, has excellent temperatures year round for an ice cream and surf shop.

> **Suggested Additional Analysis:** It would be helpful to know how the weather in Oahu has changed over the years in order to predict how future years will be:

1. The following query will obtain temperature values for a given year.

    * results = session.query(Measurement.tobs).filter(extract('year', Measurement.date) == {Insert Year}).all()

2. The following query will obtain the precipitation values for a given year.

    * results = session.query(Measurement.prcp).filter(extract('year', Measurement.date) == {Insert Year}).all()


---

## Reference Documentation - [Source Code Repository](https://github.com/Jamesrx33/Surfs-Up), [Download .zip file](https://github.com/Jamesrx33/Surfs-Up/archive/refs/heads/main.zip)

# Bellabeat Case Study: Fitbit User Behavior Analysis

This project analyzes Fitbit activity and sleep data using Python, SQL, and Tableau to identify trends in user behavior and develop data-driven recommendations for Bellabeat's marketing strategy. 

**Kaggle Notebook:** [Bellabeat Case Study](https://www.kaggle.com/code/takia2006/bellabeat-case-study-using-python-and-sql)

## Business Problem

Bellabeat is a high-tech wellness company that manufactures health-focused smart products for women. The company wants to better understand how consumers use smart fitness devices and use those insights to support future marketing decisions.

## Project Goal

The goal of this case study is to analyze Fitbit user activity and sleep data to identify behavioral trends and make recommendations that could help improve marketing and user engagement with the Bellabeat app.

## Tools Used

- Python (Pandas, NumPy)
- SQL
- Tableau
- Kaggle's Jupyter Notebooks

## Skills Demonstrated

- Data Cleaning and Transformation
- Exploratory Data Analysis (EDA)
- Analysis using Pandas and SQL
- SQL Joins and Aggregations
- Data Visualization
- Creating Data-Driven Recommendations

## Data Source

The dataset used in this project is Fitbit Fitness Tracker Data by Möbius on Kaggle, which is licensed under the CCO Public Domain. The dataset was created by respondents to a distributed survey via Amazon Mechanical Turk between 03/12/2016 and 05/12/2016. 

**Dataset:** [Fitbit Fitness Tracker Data](https://www.kaggle.com/datasets/arashnic/fitbit)

## Limitations

- The dataset contains data from a relatively small sample of Fitbit users
- Data was collected between March and May 2016, so it's outdated
- Sleep data was not available for all participants or throughout the whole time period
- The dataset represents Fitbit users and may not fully reflect Bellabeat's target customer base

## Files

- `bellabeat-case-study.ipynb` – Complete analysis notebook
- `data_preprocessing.py` – Data cleaning, transformation, and database creation
- `bellabeat_queries.sql` – SQL queries used throughout the analysis

## Key Findings
- Most users are not getting the recommended 8,000-10,000 steps and fall within the sedentary to somewhat active categories
- Saturday had the highest average activity levels, with 7,752 steps and an average intensity score of 12.33
- Sunday is the day with least activity with 6,607 steps and 10.74 intensity, but the most sleep with 7.55 hours, indicating that it's a rest day
- Users who had more sedentary minutes tended to sleep less, suggesting a potential negative relationship between sleep duration and sedentary behavior
- On weekdays, activity is affected by work schedule and most activity is from 5PM to 7PM
- On weekends, activity is more consistent throughout the day and higher from 12PM and 2PM

## My Recommendations
1) The Bellabeat marketing team should focus marketing primarily on everyday women instead of more active athletes, since that is the majority of smart fitness device users. Marketing should emphasize a woman's well-being and being healthy over being active, and everyday activities like cleaning and going to work should be acknowledged to encourage women.

2) The Bellabeat app should send motivating messages throughout the day and recommend workouts on Saturday noons and Tuesday evenings, since people are most active around these times. The Bellabeat app should send calming messages on Sunday and recommend relaxing activities like yoga to reduce stress from the week because Sunday seems to be a rest day.

3) Lastly, the Bellabeat app should give incentives for getting 8 hours of sleep and getting 8,000 steps a day. Incentives can be a streak count or points that can be used to unlock features in the app, customize the app, or can be applied to a discount for future Bellabeat purchases. The app should also encourage users to take a short walk after long periods of sedentary activity to improve sleep and help them meet the recommended daily step goals.

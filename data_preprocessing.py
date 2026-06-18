"""
Bellabeat Case Study

This script loads, cleans, merges, and transforms Fitbit activity
and sleep datasets before exporting them to a SQLite database
for analysis.

"""

import pandas as pd # data processing, CSV file I/O
import sqlite3 # to export pandas dataframes to a sql database

# --- PROCESSING DAILY ACTIVITY ---

# --- load and merge daily activities
daily_march = pd.read_csv(
    "/kaggle/input/datasets/arashnic/fitbit/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16/dailyActivity_merged.csv"
)
daily_april = pd.read_csv(
    "/kaggle/input/datasets/arashnic/fitbit/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv"
)
daily_merged = pd.concat([daily_march, daily_april], axis=0)

# --- drop duplicate 4/12/2016 entries
daily_merged = daily_merged.drop_duplicates(subset=["Id", "ActivityDate"], keep="last")

# --- fix the type of ActivityDate to datetime and add day of the week column
daily_merged["ActivityDate"] = pd.to_datetime(daily_merged["ActivityDate"], format="%m/%d/%Y")
daily_merged.insert(2, "DayOfTheWeek", daily_merged["ActivityDate"].dt.day_name())

# --- PROCESSING HOURLY ACTIVITY ---

# --- load and merge hourly activities
hourly_cal_march = pd.read_csv(
    "/kaggle/input/datasets/arashnic/fitbit/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16/hourlyCalories_merged.csv"
)
hourly_int_march = pd.read_csv(
    "/kaggle/input/datasets/arashnic/fitbit/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16/hourlyIntensities_merged.csv"
)
hourly_steps_march = pd.read_csv(
    "/kaggle/input/datasets/arashnic/fitbit/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16/hourlySteps_merged.csv"
)
hourly_cal_april = pd.read_csv(
    "/kaggle/input/datasets/arashnic/fitbit/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/hourlyCalories_merged.csv"
)
hourly_int_april = pd.read_csv(
    "/kaggle/input/datasets/arashnic/fitbit/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/hourlyIntensities_merged.csv"
)
hourly_steps_april = pd.read_csv(
    "/kaggle/input/datasets/arashnic/fitbit/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/hourlySteps_merged.csv"
)

# --- merge each month's using inner join
hourly_march = pd.merge(hourly_cal_march, hourly_int_march, on=["Id", "ActivityHour"], how="inner")
hourly_march = pd.merge(hourly_march, hourly_steps_march, on=["Id", "ActivityHour"], how="inner")

hourly_april = pd.merge(hourly_cal_april, hourly_int_april, on=["Id", "ActivityHour"], how="inner")
hourly_april = pd.merge(hourly_april, hourly_steps_april, on=["Id", "ActivityHour"], how="inner")

# --- vertically merge both months together and drop duplicates
hourly_merged = pd.concat([hourly_march, hourly_april], axis=0)
hourly_merged = hourly_merged.drop_duplicates(subset=["Id", "ActivityHour"], keep="last")

# --- fix ActivityHour to datetime type and add day of week and seperate hour column in 12-hour format to use in analysis
hourly_merged["ActivityHour"] = pd.to_datetime(hourly_merged["ActivityHour"], format="%m/%d/%Y %I:%M:%S %p")
hourly_merged["DayOfTheWeek"] = hourly_merged["ActivityHour"].dt.day_name()
hourly_merged["Hour12"] = hourly_merged["ActivityHour"].dt.strftime("%I %p")

# --- PROCESSING SLEEP DATA ---

# --- clean sleepDay, fix SleepDay column to be datetime

sleep_day = pd.read_csv(
    "/kaggle/input/datasets/arashnic/fitbit/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/sleepDay_merged.csv"
)
sleep_day["SleepDay"] = pd.to_datetime(sleep_day["SleepDay"], format="%m/%d/%Y %I:%M:%S %p")
sleep_day = sleep_day.drop_duplicates(subset=["Id", "SleepDay"], keep="last")

# --- EXPORT DATA TO SQL DATABASE ---

# --- export daily_activity, hourly_activity, sleep_day to sql database for further analysis

conn = sqlite3.connect("/kaggle/working/fitbit.db")
daily_merged.to_sql("daily_activity", conn, if_exists="replace", index=False)
hourly_merged.to_sql("hourly_activity", conn, if_exists="replace", index=False)
sleep_day.to_sql("sleep_day", conn, if_exists="replace", index=False)

conn.close()

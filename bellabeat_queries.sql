-- individual averages for each ID
SELECT da."Id",
	ROUND(AVG(da."TotalSteps"), 2) as "Avg Steps",
	ROUND(AVG(da."VeryActiveMinutes"), 2) as "Avg Very Active Mins",
	ROUND(AVG(da."FairlyActiveMinutes"), 2) as "Avg Fairly Active Mins",
	ROUND(AVG(da."LightlyActiveMinutes"), 2) as "Avg Lightly Active Mins",
    ROUND(AVG(da."FairlyActiveMinutes" + 2*da."VeryActiveMinutes"), 2) as "Avg Exercise Mins",
	ROUND(AVG(da."SedentaryMinutes"), 2) as "Sedentary Mins",
	ROUND(AVG(da."Calories"), 2) as "Avg Calories",
	ROUND(AVG(sd."TotalMinutesAsleep"), 2) as "Avg Mins Asleep"
FROM daily_activity as da
INNER JOIN sleep_day as sd
	ON da."Id" = sd."Id" 
	AND da."ActivityDate" = sd."SleepDay"
GROUP BY da."Id"
ORDER BY "Avg Steps" DESC

-- comparing hours of sleep and hours of sedentary activity
SELECT da."Id", da."ActivityDate", 
ROUND(da."SedentaryMinutes"/60.0, 2) AS "Sedentary Hours", 
da."FairlyActiveMinutes" + 2*da."VeryActiveMinutes" AS "Exercise Mins",
ROUND(sd."TotalMinutesAsleep"/60.0, 2) AS "Total Hours Asleep"
FROM daily_activity AS da
INNER JOIN sleep_day AS sd
	ON da."Id" = sd."Id"
	AND da."ActivityDate" = sd."SleepDay"
ORDER BY da."SedentaryMinutes" DESC

-- classifying users by whether or not they meet the daily recommended minutes of moderate-equivalent physical activity
SELECT "Meets Recommended Exercise?",
    COUNT("Id") AS "Number of IDs"
FROM (
    SELECT "Id",
    	CASE
            WHEN AVG("FairlyActiveMinutes" + 2*"VeryActiveMinutes") >= 21.4 THEN 'Enough Exercise'
            WHEN AVG("FairlyActiveMinutes" + 2*"VeryActiveMinutes") < 21.4 THEN 'Not Enough Exercise'
        END AS "Meets Recommended Exercise?"
    FROM daily_activity 
    GROUP BY "Id"
)
GROUP BY "Meets Recommended Exercise?"

--- classifying users by their average daily steps
SELECT "Level of Activity",
COUNT("Id") as "Number of Ids"
FROM (
	SELECT "Id", 
	ROUND(AVG("TotalSteps"), 2) AS "Avg Steps",
	CASE
		WHEN AVG("TotalSteps") < 5000 THEN 'Sedentary'
		WHEN AVG("TotalSteps") BETWEEN 5000 AND 7499 THEN 'Low Active'
		WHEN AVG("TotalSteps") BETWEEN 7500 AND 9999 THEN 'Somewhat Active'
		WHEN AVG("TotalSteps") BETWEEN 10000 AND 12499 THEN 'Active'
		WHEN AVG("TotalSteps") > 12500 THEN 'Highly Active'
	END AS "Level of Activity"
	FROM daily_activity
	GROUP BY "Id"
	) 
GROUP BY "Level of Activity"
ORDER BY "Number of IDs" DESC

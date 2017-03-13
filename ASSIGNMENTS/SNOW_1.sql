use snowflake;

SELECT *
	FROM Measurement_Facts
	WHERE phenomenon_type = "blood_pressure"
		AND timestamp >= '2015/01/01' and timestamp <= '2015/01/30'

INTO OUTFILE '/Users/yerath/tmp/1661152.1.snow.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
;
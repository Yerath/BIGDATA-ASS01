use starschema;

SELECT 
	Person.idPerson,
	Person.name,
    (
		SELECT AVG(value)
		FROM Measurement_Facts 
		WHERE phenomenon_type = "heart_rate"
		AND Person_idPerson = Person.idPerson
		AND timestamp > '2015-01-23'
        AND timestamp < '2015-01-24'
    ) as HeartRate_Average,
	(
		SELECT AVG(value)
		FROM Measurement_Facts 
		WHERE phenomenon_type = "blood_pressure"
		AND unit = "systolic"
		AND Person_idPerson = Person.idPerson
		AND timestamp > '2015-01-23'
        AND timestamp < '2015-01-24'
	) as Systolic_Average,
    (
		SELECT AVG(value)
		FROM Measurement_Facts 
		WHERE phenomenon_type = "blood_pressure"
		AND unit = "diastolic"
		AND Person_idPerson = Person.idPerson
		AND timestamp > '2015-01-23'
        AND timestamp < '2015-01-24'
	) as Diastolic_Average
FROM Measurement_Facts
JOIN Person ON Measurement_Facts.Person_idPerson = Person.idPerson
GROUP BY
	Person.name, Person.idPerson
ORDER BY
	HeartRate_Average ASC


INTO OUTFILE '/Users/yerath/tmp/1661152.3.star.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
;
    